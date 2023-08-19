from django.urls import path
from . import api_view

app_name = 'blog'

urlpatterns = [
    ## api
    path('api/list', api_view.PostListApi.as_view(), name='post_list_api'),
    path('api/list/<int:pk>', api_view.PostDetailApi.as_view(), name='post_detail_api'),
    path('api/list/filter/<str:query>', api_view.post_search_api, name='post_search_api'),
    path('category/<slug:slug>', api_view.PostsByCategory.as_view(), name='PostsByCategory'),
    path('tags/<slug:slug>', api_view.PostsByTags.as_view(), name='PostsByTags'),
]

























