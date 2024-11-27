"""
Заполняет таблицу с позициями меню
Перед заполнением блюд необходимо,
чтобы табилца с разделами меню была заполнена.
"""

from django.core.management import BaseCommand
from django.db import transaction

from foods.models import Food, FoodCategory


class Command(BaseCommand):

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write("Creating food categories")

            drinks = FoodCategory.objects.get(name_ru="Напитки")
            snacks = FoodCategory.objects.get(name_ru="Закуски")
            bakery = FoodCategory.objects.get(name_ru="Выпечка")
            dishes = FoodCategory.objects.get(name_ru="Основные блюда")

            coke, flag = Food.objects.get_or_create(
                category=drinks,
                code=100, internal_code=100, cost=100,
                name_ru="Кола",
                is_publish=True,
            )

            water, flag = Food.objects.get_or_create(
                category=drinks,
                code=115, internal_code=115, cost=80,
                name_ru="Вода минеральная",
                is_publish=True,
            )

            chips, flag = Food.objects.get_or_create(
                category=snacks,
                code=401, internal_code=401, cost=180,
                name_ru="Чипсы Lays",
                is_publish=False,
            )

            frys, flag = Food.objects.get_or_create(
                category=snacks,
                code=402, internal_code=402, cost=320,
                name_ru="Картошка фри",
                is_publish=True,
            )
            if flag:
                frys.additional.add(coke)

            venzel, flag = Food.objects.get_or_create(
                category=bakery,
                code=202, internal_code=202, cost=115,
                name_ru="Вензель с малиной",
                is_publish=False,
            )

            hachapur, flag = Food.objects.get_or_create(
                category=bakery,
                code=203, internal_code=203, cost=150,
                name_ru="Хачапури",
                is_publish=False,
            )

            burger, flag = Food.objects.get_or_create(
                category=dishes,
                code=303, internal_code=303, cost=315,
                name_ru="Бургер с котлетой из оленины",
                is_publish=True,
            )
            if flag:
                burger.additional.add(coke)
                burger.additional.add(frys)

            steak, flag = Food.objects.get_or_create(
                category=dishes,
                code=327, internal_code=327, cost=400,
                name_ru="Стейк рибай",
                is_publish=True,
            )

            self.stdout.write(self.style.SUCCESS("Foods created"))
