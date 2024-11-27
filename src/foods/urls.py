from django.urls import path

from foods.views import FoodListView, FoodCategoriesListView

app_name = 'foods'

urlpatterns = [
    # /foods/foods
    path('foods/', FoodListView.as_view(), name='food-list'),
    # foods/categories
    path('categories/',
         FoodCategoriesListView.as_view(),
         name='categories-list'),
]
