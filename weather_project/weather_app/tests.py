from django.test import TestCase
from .models import WeatherData
import pytest
from django.urls import reverse
from django.test import Client


class WeatherDataModelTest(TestCase):
    def test_weather_data_creation(self):
        weather_data = WeatherData.objects.create(temperature=25.5)
        self.assertEqual(weather_data.temperature, 25.5)


@pytest.fixture
def client():
    return Client()


def test_weather_data_list_view(client):
    WeatherData.objects.create(temperature=20.0)
    WeatherData.objects.create(temperature=25.0)
    response = client.get(reverse("weather-list"))
    assert response.status_code == 200
    assert "20.0" in str(response.content)
    assert "25.0" in str(response.content)
