from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate



from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MyUser
from .serializers import MyUserSerializer,MyUserSerializerPOST

# Create your views here.

class Login(APIView):

    def get(self, request):

        format = {
            "Format":{
                "username":"your username",
                "password":"your password",
            }
        }

        return Response(format, status=status.HTTP_200_OK)


    def post(self, request):
        username = self.request.data['username']
        password = self.request.data['password']
        print(username, password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({"message":"Has iniciado sesion correctamente"}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Credenciales incorrectas, por favor revisa tus datos"}, status=status.HTTP_400_BAD_REQUEST)
        


class Registration(APIView):

    def post(self, request):
        
        user_serializer = MyUserSerializerPOST(data=self.request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)