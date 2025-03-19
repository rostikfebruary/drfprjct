# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import NewCar
from rest_framework import status
from cars.serializers import CarSerializer,NewCarSerializer


class CarsTestView(APIView):
    def get(self, *args, **kwargs):
        cars = NewCar.objects.all()
        serializer = NewCarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CarCrud(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        car = NewCar.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = NewCar.objects.get(pk=pk)
        except NewCar.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = NewCar.objects.get(pk=pk)
        except NewCar.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            NewCar.objects.get(pk=pk).delete()
        except NewCar.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        return Response(status=status.HTTP_404_NOT_FOUND)
