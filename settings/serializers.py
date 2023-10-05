from rest_framework import serializers
from .models import Settings
from parler_rest.serializers import TranslatableModelSerializer


class SettingsSerializer(TranslatableModelSerializer):
    class Meta:
        model = Settings
        fields = ['site_header',
                  'phone',
                  'email',
                  'description',
                  'logo',
                  'fb_link',
                  'twitter_link',
                  'instagram_link',
                  'linkedin_link']










































































