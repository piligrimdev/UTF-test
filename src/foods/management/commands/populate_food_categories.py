"""
Заполняет таблицу с разделами меню
"""

from django.core.management import BaseCommand
from django.db import transaction

from foods.models import FoodCategory

class Command(BaseCommand):
    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write("Creating food categories")

            drinks, flag = FoodCategory.objects.get_or_create(
                name_ru="Напитки", name_en="Drinks", name_ch="饮料",
                order_id=10
            )

            bakery, flag = FoodCategory.objects.get_or_create(
                name_ru="Выпечка", name_en="Bakery", name_ch="面包店",
                order_id=20
            )

            main_dishes, flag = FoodCategory.objects.get_or_create(
                name_ru="Основные блюда", name_en="Main dishes", name_ch="主菜",
                order_id=30
            )

            snacks, flag = FoodCategory.objects.get_or_create(
                name_ru="Закуски", name_en="Snaks", name_ch="零食",
                order_id=40
            )

            alco, flag = FoodCategory.objects.get_or_create(
                name_ru="Алкоголь", name_en="Alc.",
                order_id=50
            )

            self.stdout.write(self.style.SUCCESS("Food categories created"))
