from .serializers import Account
from rest_framework import serializers
from property.serializers import GettingReservationsSerializer, GettingReviewSerializer, ReadFavoriteSerializer

class AccountSerializer(serializers.ModelSerializer):
    reservations = GettingReservationsSerializer(many=True, read_only=True, source='client_reservations')
    reviews = GettingReviewSerializer(many=True, read_only=True, source='client_reviews')
    favs = ReadFavoriteSerializer(many=True, read_only=True, source='client_favorites')
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
                  'reservations',
                  'reviews',
                  'favs']
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












































