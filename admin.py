from django.contrib import admin
from .models import Sensor, SensorData, Alert

admin.site.register(Sensor)
admin.site.register(SensorData)
admin.site.register(Alert)
