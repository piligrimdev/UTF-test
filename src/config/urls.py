from django.contrib import admin
from django.urls import path, include
from api.views import custom404

handler404 = custom404

urlpatterns = [
    path('admin/', admin.site.urls),
    # для api запроса
    path('api/', include('api.urls')),
]
