from django.urls import path
from . import api_view



app_name = 'accounts'

urlpatterns = [
    path('sign-up/', api_view.SignUp.as_view(), name='sign-up'),
    path('sign-in/', api_view.Login.as_view(), name='sign-in'),
    path('myprofile/', api_view.UserProfile.as_view(), name='myprofile'),
    path('myprofile/<int:pk>/', api_view.AccountView.as_view(), name='changeprofile'),
]














