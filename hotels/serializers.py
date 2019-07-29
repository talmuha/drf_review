from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Hotel, Booking

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'location', 'price_per_night']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['check_in', 'number_of_nights']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password',]

    def create(self, validated_data):
        my_username = validated_data['username']
        my_password = validated_data['password']
        new_user = User(username=my_username)
        new_user.set_password(my_password)
        new_user.save()
        return validated_data
