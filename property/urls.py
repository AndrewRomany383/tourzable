from django.urls import path
from .views import PropertyList, PropertyDetail
from . import api_view


app_name = 'property'

urlpatterns = [
    path('property/', PropertyList.as_view(), name='property_list'),
    path('property/<slug:slug>', PropertyDetail.as_view(), name='property_detail'),
    ## api
    path('api/list', api_view.PropertyApiList.as_view(), name='PropertyApiList'),
    path('api/list/<int:pk>', api_view.PropertyApiDetail.as_view(), name='PropertyApiDetail'),
    path('api/category', api_view.Categories.as_view(), name='Categories'),
    path('api/category/<str:slug>', api_view.PropertyByCategory.as_view(), name='PropertyByCategory'),
    path('api/places', api_view.Places.as_view(), name='places'),
    path('api/places/<str:slug>', api_view.PropertyByPlace.as_view(), name='PropertyByPlace'),
    path('api/inquiry', api_view.Inquiry.as_view(), name='inquiry'),
    path('api/visa', api_view.VisaSubmit.as_view(), name='visa')
]