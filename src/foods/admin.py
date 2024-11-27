from django.contrib import admin

from foods.models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = "name_ru", "code", "is_publish", "cost", "category_name_ru"
    list_display_links = "name_ru",
    filter_horizontal = ('additional',)

    search_fields = "name_ru",

    def get_queryset(self, request):
        return Food.objects.prefetch_related("category")

    def category_name_ru(self, obj) -> str:
        return obj.category.name_ru


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = "name_ru", "order_id",
    list_display_links = "name_ru",

    search_fields = "name_ru",
