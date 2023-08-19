from rest_framework import serializers
from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ['id']



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


















