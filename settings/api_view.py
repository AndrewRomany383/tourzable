from .serializers import SettingsSerializer
from .models import Settings
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from property.models import Property, Place, Category
from property.serializers import PropertySerializer, PlaceSerializer, CategorySerializer
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from blog.serializers import PostSerializer



@api_view(['GET'])
def home(request):
    places = Place.objects.only('name', 'image').annotate(property_count=Count('property_place'))
    category = Category.objects.only('name')
    category_list = Property.objects.select_related('category')
    recent_posts = Post.objects.only('slug', 'title', 'tags', 'image')
    data_property = PropertySerializer(category_list, many=True).data
    data_category = CategorySerializer(category, many=True).data
    data_places = PlaceSerializer(places, many=True, context={'request':request}).data
    data_recent_posts = PostSerializer(recent_posts, many=True, context={'request':request}).data
    return Response({'data_property':data_property,
                     'data_category':data_category,
                     'data_places':data_places,
                     'data_recent_posts':data_recent_posts})




"""@api_view(['GET'])
def home(request):
    places = Place.objects.only('name','image').annotate(property_count=Count('property_place'))
    category = Category.objects.only('name')
    category_list = Property.objects.filter(Property_category__name=Property.category.name)
    category_list_count = Property.objects.filter(category_name=Property.category.name).Count()
    recent_posts = Post.objects.only('slug','title','tags','image')
    data_property = PropertySerializer(category_list, many=True).data
    data_category = CategorySerializer(category, many=True).data
    data_category_count = PropertySerializer(category_list_count).data
    data_places = PlaceSerializer(places, many=True, context={'request':request}).data
    data_recent_posts = PostSerializer(recent_posts, many=True, context={'request':request}).data
    return Response({'data_property':data_property,
                     'data_category':data_category,
                     'data_places':data_places,
                     'data_recent_posts':data_recent_posts,
                     'data_category_count':data_category_count})"""



@api_view(['GET'])
def home_search(request, query):
    place_list = Place.objects.filter(
        Q(name__icontains=query)
    )
    search = PlaceSerializer(place_list, many=True, context={'request':request}).data
    return Response({'search':search})


@api_view(['GET'])
def category_filter(request, category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    data = PropertySerializer(property_list, many=True, context={'request':request}).data
    return Response({'data':data})
















































