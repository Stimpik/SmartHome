from rest_framework import serializers

from measurement.models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'photo']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sensor
        fields = ['id', 'name', 'description',]


class SensordescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sensor
        fields = ['description']

class CreateMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'sensor', 'photo']