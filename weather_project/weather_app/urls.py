from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.weather_data, name='weather_data'),
    path('cats/', views.cats_data, name='cats_data'),
    path('catweather/', views.cats_n_weather, name='cats_n_weather'),
]