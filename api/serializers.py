from rest_framework import serializers
from .models import Advisor,User,Booking
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['id','advisorname','picture']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','username','userid','advisorname','advisorid','time',]
# class BookingDtailsSerializer(serializers.ModelSerializer):
