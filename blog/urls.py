from django.urls import path
from . import api_view

app_name = 'blog'

urlpatterns = [
    ## api
    path('api/list', api_view.PostListApi.as_view(), name='post_list_api'),
    path('api/list/ar', api_view.PostListApiAR.as_view(), name='post_list_api_ar'),
    path('api/list/<int:pk>', api_view.PostDetailApi.as_view(), name='post_detail_api'),
    path('api/list/ar/<int:pk>', api_view.PostDetailApiAR.as_view(), name='post_detail_api_ar'),
    path('category/<str:slug>', api_view.PostsByFilters.as_view(), name='PostsByCategory'),
    path('category/ar/<str:slug>', api_view.PostsByFiltersAR.as_view(), name='PostsByCategory'),
]

























