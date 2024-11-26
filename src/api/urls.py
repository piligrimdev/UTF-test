from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import FoodsByCategoryViewSet

app_name = 'api'

router = DefaultRouter()
router.register('foods', FoodsByCategoryViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),  # Адрес для API запроса:  /api/v1/foods/
]
