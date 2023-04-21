# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, SensordescriptionSerializer, \
    MeasurementSerializer, CreateMeasurementSerializer


class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        ser = SensorSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status='201')
        return Response(ser.data, status='500')



class RetrieveUpdateAPIView(APIView):

    def get(self, request, pk):

        sensor = Sensor.objects.get(id=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)


    def patch(self,request, pk):

        sensor = Sensor.objects.get(id=pk)

        serializer = SensordescriptionSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status='201')
        return Response(serializer.data, status='500')

class CreateAPIView(APIView):

    def post(self, request):
        serializer = CreateMeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status='201')
        return Response(serializer.data, status='500')
