from django.shortcuts import render, get_object_or_404
from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogSerializerPOST, BlogSerializerGET
from authentication.models import MyUser


# Create your views here.

class GETBlogView(APIView):
        
    def get(self, request, format = None):
        blog = Blog.objects.filter(author=request.user.id)
        blog_serializer = BlogSerializerGET(blog, many = True)
        return Response(blog_serializer.data, status=status.HTTP_200_OK)


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
        


class PUTBlogView(APIView):

    def get_object(self, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            return blog
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.author == request.user:
            blog_serializer = BlogSerializerPOST(blog)
            return Response(blog_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No tienes permiso para editar este blog"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.author == request.user:
            blog_serializer = BlogSerializerPOST(blog, data=request.data, partial=True)
            if blog_serializer.is_valid():
                blog_serializer.save()
                return Response(blog_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Los datos ingresados no son válidos"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No tienes permiso para editar este blog"}, status=status.HTTP_403_FORBIDDEN)

    def handle_exception(self, exc):
        return Response({"error": str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class DELETEBlogView(APIView):
    def get_object(self, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            return blog
        except Blog.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.author == request.user:
            blog_serializer = BlogSerializerPOST(blog)
            return Response(blog_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No tienes permiso para editar este blog"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk, format=None):
        blog = self.get_object(pk)
        if blog.author == request.user:
            blog.delete()
            return Response({"message": "El blog ha sido eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "No tienes permiso para eliminar este blog"}, status=status.HTTP_403_FORBIDDEN)