from rest_framework import serializers
from cars.models import NewCar


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    v = serializers.FloatField()

    def create(self, validated_data):
        car = NewCar.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class NewCarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
