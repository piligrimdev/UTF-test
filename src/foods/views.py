"""
View для просмотра всех существующих блюд и разделов меню.
Выводят на простых html страницах.
"""


from django.views.generic import ListView

from foods.models import Food, FoodCategory


class FoodListView(ListView):
    template_name = 'foods/foods.html'
    model = Food
    context_object_name = "foods"


class FoodCategoriesListView(ListView):
    template_name = 'foods/categories.html'
    model = FoodCategory
    context_object_name = "categories"
