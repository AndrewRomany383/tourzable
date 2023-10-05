from django.urls import path
from . import api_view


app_name = 'settings'

urlpatterns = [
    path('', api_view.home, name='home'),
    path('ar', api_view.home_ar, name='home_ar'),
    path('category_filter/<str:query>', api_view.home_search_and_category_filter, name='category_filter'),
    path('category_filter_ar/<str:query>', api_view.home_search_and_category_filter_ar, name='category_filter_ar')
]




































