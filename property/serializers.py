from rest_framework import serializers
from .models import Property, Place, Category, PropertyAvailabilityCheck, Visa, PropertyImages



class PropertyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImages
        exclude = ['id']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['name',
                  'image',
                  'price_of_single_room_by_person',
                  'price_of_double_room_by_person',
                  'price_of_triple_room_by_person',
                  'price_of_single_room_by_night',
                  'price_of_double_room_by_night',
                  'price_of_triple_room_by_night',
                  'description',
                  'place',
                  'created_at',
                  'slug',
                  'category']

class PropertyDetailSerializer(serializers.ModelSerializer):
    propertyimages = PropertyImagesSerializer(many=True, read_only=True, source='property_image')
    class Meta:
        model = Property
        fields = ['name',
                  'image',
                  'price_of_single_room_by_person',
                  'price_of_double_room_by_person',
                  'price_of_triple_room_by_person',
                  'price_of_single_room_by_night',
                  'price_of_double_room_by_night',
                  'price_of_triple_room_by_night',
                  'description',
                  'place',
                  'created_at',
                  'slug',
                  'category',
                  'propertyimages']


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        exclude = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']

class PropertyAvailabilityCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAvailabilityCheck
        exclude = ['id']

class VisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visa
        exclude = ['id']


















