from django.db.models import Prefetch
from django.http import JsonResponse
from django.views import defaults
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from foods.models import Food, FoodCategory

from api.serializers import FoodSerializer, FoodListSerializer

class FoodsByCategoryViewSet(GenericViewSet):
    """
    ViewSet для запроса пунктов меню
    """
    queryset = (FoodCategory.objects.prefetch_related(
                Prefetch('food', queryset=Food.objects.filter(is_publish=True)))
                .order_by('id'))   # подгружаем позиции сразу и фильтруем по полю is_publish
                                   # для большей наглядности сортируем по id

    serializer_class = FoodListSerializer

    def list(self, request, *args, **kwargs):
        data = FoodListSerializer(self.queryset, many=True).data

        result = [x for x in data if len(x['foods']) > 0]
        # из сериализованных данных сохраняем только те, где
        # список "foods" содержит хотя бы 1 элемент.

        return Response(result)


def custom404(request, exception=None):
    if request.headers.get("ACCEPT") == "application/json":
        return JsonResponse({
            'status_code': 404,
            'error': 'The resource was not found'
        })

    return defaults.page_not_found(request)
