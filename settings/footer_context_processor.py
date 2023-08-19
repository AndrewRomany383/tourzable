from .serializers import SettingsSerializer
from .models import Settings
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

class Myfooter(ListCreateAPIView):
    queryset = Settings.objects.only('description', 'fd_link', 'twitter_link', 'instagram_link')
    serializer_class = SettingsSerializer