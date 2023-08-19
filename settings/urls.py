from django.urls import path
from . import api_view


app_name = 'settings'

urlpatterns = [
    path('', api_view.home, name='home'),
    path('home_search/<str:query>', api_view.home_search, name='home_search'),
    path('category_filter/<str:category>', api_view.category_filter, name='category_filter')
]




































