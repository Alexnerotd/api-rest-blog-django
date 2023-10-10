from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import MyUser


class MyUserSerializer(ModelSerializer):


    class Meta:
        model = MyUser
        fields = ['username','password']


class MyUserSerializerPOST(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username','email','password','name']


    def create(self, validate_data):
        user = MyUser(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user