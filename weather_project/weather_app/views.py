from django.shortcuts import render
import requests
from django.http import HttpResponse

# from google.cloud import datastore
from .models import WeatherData
from django.views.generic import ListView


def fetch_weather_data(request):
    # current temperature for Warsaw (latitude 52,2298, longitude 21,0118)
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.0118&current_weather=true"
    )
    data = response.json().get("current_weather")
    temperature = data.get("temperature", "")
    datetime = data.get("time", "")
    if datetime and temperature:
        # comment this function before running app (empty sdk variables)
        # store_data_in_google_cloud(temperature, datetime)
        store_data_in_db(temperature, datetime)
    return HttpResponse("temperature fetched and saved successfully!")


# looks like google cloud sdk is not free so i will left google variables empty
def store_data_in_google_cloud(temperature, datetime):
    data = {"temperature": temperature, "date": datetime}
    # client = datastore.Client("project_id")
    # entity = datastore.Entity(key=client.key("weather_data"))
    # entity.update(data)
    # client.put(entity)


def store_data_in_db(temperature, datetime):
    weather_data_db = WeatherData(temperature=temperature, time=datetime)
    weather_data_db.save()


class WeatherListView(ListView):
    model = WeatherData
    template_name = "weather_list.html"
