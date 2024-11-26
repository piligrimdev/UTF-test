from django.urls import path

from foods.views import FoodListView, FoodCategoriesListView

app_name = 'foods'

urlpatterns = [
    path('foods/', FoodListView.as_view(), name='food-list'),  # /foods/foods
    path('categories/', FoodCategoriesListView.as_view(), name='categories-list'),  # foods/categories
]
