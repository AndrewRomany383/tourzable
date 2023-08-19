from django.urls import path
from . import api_view



app_name = 'accounts'

urlpatterns = [
    path('register/', api_view.SignUp.as_view(), name='register'),
    path('login/', api_view.Login.as_view(), name='login'),
    path('myprofile/', api_view.UserProfile.as_view(), name='myprofile'),
    path('myprofile/<int:pk>/', api_view.AccountView.as_view(), name='changeprofile'),
]














