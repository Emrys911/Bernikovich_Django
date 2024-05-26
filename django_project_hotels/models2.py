from django.db import models
from rest_framework import serializers
from models import Hobby
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import HotelOwnerSerializer


class HotelOwnerListCreateAPIView(APIView):
    # GET для получения списка и POST для создания
    pass


class HotelOwnerRetrieveUpdateAPIView(APIView):
    # GET для получения одного объекта, PUT для обновления
    pass


class HotelOwnerDeleteAPIView(APIView):
    # DELETE для удаления объекта
    pass


class HotelOwnerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    hotel_name = serializers.CharField(max_length=100)

    def create(self, validated_data):  # создание нового владельца отеля
        return HotelOwner(**validated_data)

    def update(self, isinstance, validated_data):  # обновление информации о владельце отеля
        isinstance.name = validated_data.get('name', instance.name)
        return isinstance


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['name', 'description']


class BaseHotelModel:
    pass


class BaseHotelModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        class Hotel(BaseHotelModel):
            name = models.CharField(max_length=100, db_index=True)


class Owner(BaseHotelModel):
    name = models.CharField(max_length=50)

    class Person(models.Model):
        name = models.CharField(max_length=100, db_index=True)
        age = models.IntegerField(db_index=True)

    class Meta:
        indexes = [models.Index(fields=['name']),
                   models.Index(fields=['age']),
                   models.Index(fields=['hobby']),
                   models.Index(fields=['comments_users']), ]


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    class Meta:
        indexes = {
            models.Index(fields=['name']),
            models.Index(fields='location'),
            models.Index(fields='coments_hotel'),
        }


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_full_name = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_full_name = models.CharField(max_length=255)
