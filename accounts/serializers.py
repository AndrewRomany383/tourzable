from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'password',
                  'email',
                  'phone_number',
                  'profile_image',
                  'language',
                  'reservations']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = Account.objects.create(**validated_data)
        password = validated_data.get("password")
        user.set_password(password)
        user.save()
        return user

class AccountPorfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'phone_number',
                  'profile_image',
                  'language']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def validate(self, attrs):
            return attrs

        def create(self, validated_data):
            user = validated_data.get(**validated_data)
            password = validated_data.get("password")
            user.set_password(password)
            user.save()
            return user

"""def update(self,Account, validated_data):
    user = Account.objects.aupdate_or_create(**validated_data)
    user.save()
    return user"""



"""class ClientUserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = ClientUserProfile
        fields = ['username',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'profile_image',
                  'language']

    def create(self, validated_data):
        password = validated_data.get("password")
        user = ClientUserProfile.objects.create(**validated_data)
        user.set_password(password)
        return user




class TourGuideUserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = TourGuideUserProfile
        fields = ['username',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  'phone_number',
                  'profile_image',
                  'language']

    def create(self, validated_data):
        password = validated_data.get("password")
        user = TourGuideUserProfile.objects.create(**validated_data)
        user.set_password(password)
        return user"""












































































