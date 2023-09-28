from django.urls import path
from .views import WeatherListView, fetch_weather_data

urlpatterns = [
    path("fetched_weather_data_list/", WeatherListView.as_view(), name="weather-list"),
    path("fetch_weather_data/", fetch_weather_data, name="fetch-weather-data"),
]
