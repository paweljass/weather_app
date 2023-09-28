from django.db import models


class WeatherData(models.Model):
    temperature = models.CharField(max_length=24)
    time = models.DateTimeField()
