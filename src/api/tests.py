from django.db.models import Prefetch

from rest_framework.test import APITestCase
from rest_framework import status

from foods.models import Food, FoodCategory

from api.serializers import FoodListSerializer


class FilteredFoodAPITest(APITestCase):
    fixtures = ['test_fixtures.json']

    def test_api_request_returns_filtered_foods(self):
        url = '/api/v1/foods/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        list_foods_by_category = response.json()

        self.assertEqual(len(list_foods_by_category), 3)
        # в выборке не попадают категории алкоголь ( нет позиций вообще )
        # и выпечка ( обе позиции имеют значения is_publish=False )

        self.assertEqual(len(list_foods_by_category[-1]['foods']), 1)
        # в категории закуски только 1 позиция из 2 имеет значение is_publish=True

        self.assertEqual(len(list_foods_by_category[0]['foods']), 2)
        # в категории напитки 2 позиции из 2 имеют значение is_publish=True

        total_foods_count = 0

        for i in list_foods_by_category:
            total_foods_count += len(i['foods'])
        self.assertEqual(total_foods_count, 5)
        # всего 5 позиций имеют значение is_publish=True

        queryset = (FoodCategory.objects.prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True)))
                    .order_by('id'))

        db_data = FoodListSerializer(queryset, many=True).data
        db_data = [x for x in db_data if len(x['foods']) > 0]

        self.assertEqual(db_data, list_foods_by_category)
        # запрос напрямую идентичен тому, что возвращает API

    def test_select_foods(self):
        foods = Food.objects.all()

        self.assertEqual(len(foods), 8)
        # всего 8 позиций в меню
