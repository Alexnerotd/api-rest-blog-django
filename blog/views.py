from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogSerializerPOST

# Create your views here.

class POSTBlogView(APIView):

    def get(self, request):
        format = {
            "title":"dataChar(required)",
            "description":"dataChar(required)",
            "content":"dataText(required)",
        }

        return Response(format, status=status.HTTP_200_OK)
    
    def post(self, request):
        blog_serializer = BlogSerializerPOST(data=self.request.data, context={'request':request})

        if blog_serializer.is_valid():
            blog_serializer.save()
            return Response({"message":"Blog creado correctamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"Los datos ingresados son incorrectos"}, status=status.HTTP_400_BAD_REQUEST)