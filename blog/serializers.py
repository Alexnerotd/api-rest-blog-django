from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Blog

class BlogSerializerPOST(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title', 'description', 'content']


    def create(self, validate_data):

        user = self.context['request'].user

        blog = Blog.objects.create(author=user, **validate_data)
        return blog
     