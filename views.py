from django.shortcuts import render, redirect
from .models import Sensor, SensorData, Alert
from .forms import SensorForm


def dashboard(request):
    sensors = Sensor.objects.count()
    data_count = SensorData.objects.count()
    alerts = Alert.objects.all().order_by('-created_at')[:5]

    context = {
        'sensors': sensors,
        'data_count': data_count,
        'alerts': alerts
    }

    return render(request, 'monitoring/dashboard.html', context)

def sensor_list(request):
    sensors = Sensor.objects.all()

    return render(request, 'monitoring/sensors.html', {
        'sensors': sensors
    })

def add_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('sensors')
    else:
        form = SensorForm()

    return render(request, 'monitoring/add_sensor.html', {
        'form': form
    })

def anomalies(request):
    alerts = Alert.objects.all().order_by('-created_at')

    return render(request, 'monitoring/anomalies.html', {
        'alerts': alerts
    })
