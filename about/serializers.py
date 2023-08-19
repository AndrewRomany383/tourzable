from rest_framework import serializers
from .models import About, FAQ


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        exclude = ['id']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ['id']































