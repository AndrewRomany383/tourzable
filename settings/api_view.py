from .serializers import SettingsSerializer
from .models import Settings
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from property.models import Trip, Place, Category
from property.serializers import PlaceSerializer, CategorySerializer, TripSerializerMultiLanguage, PlaceSerializerMultiLanguage, CategorySerializerMultiLanguage
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from blog.serializers import PostSerializer


@api_view(['GET'])
def home(request):
    settings = Settings.objects.language('en-us').only('translations', 'logo', 'fb_link', 'twitter_link', 'instagram_link', 'linkedin_link')
    places = Place.objects.language('en-us').only('translations__title', 'image').annotate(property_count=Count('property_place'))
    category = Category.objects.language('en-us').only('translations__title')
    category_list = Trip.objects.language('en-us').select_related('category')
    recent_posts = Post.objects.language('en-us').only('translations')
    data_settings = SettingsSerializer(settings, many=True, context={'request':request}).data
    data_property = TripSerializerMultiLanguage(category_list, many=True, context={'request':request}).data
    data_category = CategorySerializer(category, many=True).data
    data_places = PlaceSerializer(places, many=True, context={'request':request}).data
    data_recent_posts = PostSerializer(recent_posts, many=True, context={'request':request}).data
    return Response({'website settings':data_settings,
                     'data trips':data_property,
                     'data categories':data_category,
                     'data places':data_places,
                     'data recent_posts':data_recent_posts})


@api_view(['GET'])
def home_ar(request):
    settings = Settings.objects.language('ar-sa').only('translations', 'logo', 'fb_link', 'twitter_link', 'instagram_link', 'linkedin_link')
    places = Place.objects.language('ar-sa').only('translations__title', 'image').annotate(property_count=Count('property_place'))
    category = Category.objects.language('ar-sa').only('translations')
    category_list = Trip.objects.language('ar-sa').select_related('category').active_translations()
    recent_posts = Post.objects.language('ar-sa').only('translations')
    data_settings = SettingsSerializer(settings, many=True, context={'request':request}).data
    data_property = TripSerializerMultiLanguage(category_list, many=True, context={'request':request}).data
    data_category = CategorySerializer(category, many=True).data
    data_places = PlaceSerializer(places, many=True, context={'request':request}).data
    data_recent_posts = PostSerializer(recent_posts, many=True, context={'request':request}).data
    return Response({'website settings':data_settings,
                     'data trips':data_property,
                     'data categories':data_category,
                     'data places':data_places,
                     'data recent_posts':data_recent_posts})



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



"""@api_view(['GET'])
def home_search(request, query):
    place_list = Place.objects.language('en-us').filter(
        Q(translations__title__icontains=query)
    )
    search = PlaceSerializerMultiLanguage(place_list, many=True, context={'request':request}).data
    return Response({'search':search})

@api_view(['GET'])
def home_search_ar(request, query):
    place_list = Place.objects.language('ar-sa').filter(
        Q(title__icontains=query)
    )
    search = PlaceSerializer(place_list, many=True, context={'request':request}).data
    return Response({'search':search})"""


@api_view(['GET'])
def home_search_and_category_filter(request, query):
    try:
        category = Category.objects.language('en-us').get(translations__title=query)
        property_list = Trip.objects.language('en-us').filter(category=category)
        data = TripSerializerMultiLanguage(property_list, many=True, context={'request':request}).data
        return Response({'category filter': data})
    except:
        place_list = Place.objects.language('en-us').filter(
            Q(translations__title__icontains=query)
        )
        data2 = PlaceSerializer(place_list, many=True, context={'request':request}).data
        return Response({'place search': data2})



@api_view(['GET'])
def home_search_and_category_filter_ar(request, query):
    try:
        category = Category.objects.language('ar-sa').get(translations__title=query)
        property_list = Trip.objects.language('ar-sa').filter(category=category)
        data = TripSerializerMultiLanguage(property_list, many=True, context={'request':request}).data
        return Response({'category filter': data})
    except:
        place_list = Place.objects.language('ar-sa').filter(
            Q(translations__title__icontains=query)
        )
        data2 = PlaceSerializer(place_list, many=True, context={'request':request}).data
        return Response({'place search': data2})


"""@api_view(['GET'])
def category_filter_ar(request, category):
    category = Category.objects.language('ar-sa').get(name=category)
    property_list = Trip.objects.filter(category=category)
    data = TripSerializer(property_list, many=True, context={'request':request}).data
    return Response({'data':data})"""














































