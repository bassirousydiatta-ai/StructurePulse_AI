from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sensor, SensorData, Alert


@api_view(['POST'])
def receive_data(request):
    sensor_id = request.data.get('sensor_id')
    vibration = request.data.get('vibration')
    temperature = request.data.get('temperature')
    humidity = request.data.get('humidity')

    sensor = Sensor.objects.get(id=sensor_id)

    data = SensorData.objects.create(
        sensor=sensor,
        vibration=vibration,
        temperature=temperature,
        humidity=humidity
    )

    if float(vibration) > 80:
        Alert.objects.create(
            sensor=sensor,
            message='Vibration anormale détectée',
            danger_level='Élevé'
        )

    return Response({
        'message': 'Données reçues'
    })



"""from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sensor
from .models import SensorData
from .models import Alert

from .ai_model import predict_risk


@api_view(['POST'])
def receive_data(request):

    sensor_id = request.data.get('sensor_id')

    vibration = float(request.data.get('vibration'))
    temperature = float(request.data.get('temperature'))
    humidity = float(request.data.get('humidity'))

    sensor = Sensor.objects.get(id=sensor_id)

    SensorData.objects.create(
        sensor=sensor,
        vibration=vibration,
        temperature=temperature,
        humidity=humidity
    )

    risk = predict_risk(
        vibration,
        temperature,
        humidity
    )

    if risk > 0.7:

        Alert.objects.create(
            sensor=sensor,
            message='Anomalie détectée par IA',
            danger_level='Critique'
        )

    return Response({
        'status': 'success',
        'risk': risk
    })
"""














from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import Sensor
from .models import SensorData
from .models import Alert

from .ai_model import predict_risk


@api_view(['POST'])

def receive_data(request):

    sensor_id = request.data.get(
        'sensor_id'
    )

    vibration = float(
        request.data.get('vibration')
    )

    temperature = float(
        request.data.get('temperature')
    )

    humidity = float(
        request.data.get('humidity')
    )

    sensor = Sensor.objects.get(
        id=sensor_id
    )

    SensorData.objects.create(

        sensor=sensor,

        vibration=vibration,

        temperature=temperature,

        humidity=humidity

    )

    result = predict_risk(

        vibration,
        temperature,
        humidity

    )

    # IA détecte danger

    if result['prediction'] == 1:

        Alert.objects.create(

            sensor=sensor,

            message='Danger détecté par IA',

            danger_level='Critique'

        )

    return Response({

        'status': 'success',

        'prediction': result['prediction'],

        'risk_probability': result['probability']

    })

