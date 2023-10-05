from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from .models import About, FAQ, ContactUs, ContactConsultant



class AboutSerializer(TranslatableModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class FAQSerializer(TranslatableModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class ContactConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactConsultant
        fields = '__all__'



























