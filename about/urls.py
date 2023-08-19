from django.urls import path
from . import api_view


app_name = 'about'

urlpatterns = [
    path('about/<int:pk>/', api_view.AboutData.as_view(), name='about'),
    path('faq/<int:pk>/', api_view.FaqData.as_view(), name='faq')
]