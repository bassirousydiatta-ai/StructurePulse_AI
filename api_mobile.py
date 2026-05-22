from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import SensorData

from .serializers import SensorDataSerializer


@api_view(['GET'])
def mobile_data(request):

    data = SensorData.objects.all()

    serializer = SensorDataSerializer(
        data,
        many=True
    )

    return Response(serializer.data)