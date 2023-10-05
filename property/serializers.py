from rest_framework import serializers
from .models import Trip, Place, Category, PropertyAvailabilityCheck, Visa, TripGallery, Reservations, Reviews, Favorites
from accounts.serializers import AccountPorfileSerializer
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField



class PlaceSerializerMultiLanguage(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Place)
    class Meta:
        model = Place
        fields = ['id', 'title', 'image', 'translations']


class CategorySerializerMultiLanguage(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)
    class Meta:
        model = Category
        fields = ['id', 'title', 'translations']


class PlaceSerializer(TranslatableModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'title', 'image']


class CategorySerializer(TranslatableModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TripGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = TripGallery
        fields = '__all__'

class TripSerializerTranslated(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Trip)
    class Meta:
        model = Trip
        fields = ['id',
                  'stars',
                  'image',
                  'price_of_single_room_by_person_night',
                  'price_of_double_room_by_person_night',
                  'price_of_triple_room_by_person_night',
                  'price_of_single_room_by_night',
                  'price_of_double_room_by_night',
                  'price_of_triple_room_by_night',
                  'created_at',
                  'number_of_guests',
                  'number_of_rooms',
                  'duration',
                  'check_in',
                  'check_out',
                  'price_per_child',
                  'translations']


class TripSerializerMultiLanguage(TranslatableModelSerializer):
    place = PlaceSerializerMultiLanguage()
    category = CategorySerializerMultiLanguage()
    class Meta:
        model = Trip
        fields = ['id',
                  'title',
                  'stars',
                  'image',
                  'price_of_single_room_by_person_night',
                  'price_of_double_room_by_person_night',
                  'price_of_triple_room_by_person_night',
                  'price_of_single_room_by_night',
                  'price_of_double_room_by_night',
                  'price_of_triple_room_by_night',
                  'created_at',
                  'number_of_guests',
                  'number_of_rooms',
                  'duration',
                  'check_in',
                  'check_out',
                  'price_per_child',
                  'description',
                  'place',
                  'slug',
                  'category',
                  'trip_summary',
                  'accommodation',
                  'includes_and_excludes',
                  'itinerary',
                  'cancellation_policy',
                  'terms_conditions',
                  'notes']


class PropertyDetailSerializer(TranslatableModelSerializer):
    place = PlaceSerializerMultiLanguage()
    category = CategorySerializerMultiLanguage()
    propertyimages = TripGallerySerializer(many=True, read_only=True, source='TripGallery_images')
    class Meta:
        model = Trip
        fields = ['id',
                  'title',
                  'stars',
                  'image',
                  'price_of_single_room_by_person_night',
                  'price_of_double_room_by_person_night',
                  'price_of_triple_room_by_person_night',
                  'price_of_single_room_by_night',
                  'price_of_double_room_by_night',
                  'price_of_triple_room_by_night',
                  'created_at',
                  'number_of_guests',
                  'number_of_rooms',
                  'duration',
                  'check_in',
                  'check_out',
                  'price_per_child',
                  'description',
                  'place',
                  'slug',
                  'category',
                  'trip_summary',
                  'accommodation',
                  'includes_and_excludes',
                  'itinerary',
                  'cancellation_policy',
                  'terms_conditions',
                  'notes',
                  'propertyimages']




class PropertyAvailabilityCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAvailabilityCheck
        exclude = ['user']

class VisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visa
        fields = ['id', 'email','number_phone','visa', 'photo']



class VisaUserSerializer(serializers.ModelSerializer):
    user = AccountPorfileSerializer()
    class Meta:
        model = Visa
        fields = ['id', 'user', 'visa', 'photo']


class PlaceListSerializer(TranslatableModelSerializer):
    property = TripSerializerTranslated(many=True, read_only=True, source='property_place')
    class Meta:
        model = Place
        fields = ['id', 'title', 'image', 'property']


class CategoryListSerializer(TranslatableModelSerializer):
    category = TripSerializerTranslated(many=True, read_only=True, source='property_category')
    class Meta:
        model = Category
        fields = ['id', 'title', 'category']

class TripSerializerAllTranslated(TranslatableModelSerializer):
    place = PlaceSerializerMultiLanguage()
    category = CategorySerializerMultiLanguage()
    translations = TranslatedFieldsField(shared_model=Trip)
    class Meta:
        model = Trip
        fields = ['place',
                  'category',
                  'translations']

class ReservationsSerializer(serializers.ModelSerializer):
    trip = serializers.PrimaryKeyRelatedField(queryset=Trip.objects.only('id'))
    class Meta:
        model = Reservations
        fields = ['id',
                  'status',
                  'adult_number',
                  'guests_info',
                  'children_number_and_their_age',
                  'infant',
                  'notes',
                  'created_at',
                  'trip']
        extra_kwargs = {
            'status': {'read_only': True},
        }


class GettingReservationsSerializer(serializers.ModelSerializer):
    trip = TripSerializerMultiLanguage()
    class Meta:
        model = Reservations
        fields = ['id',
                  'status',
                  'adult_number',
                  'guests_info',
                  'children_number_and_their_age',
                  'infant',
                  'notes',
                  'created_at',
                  'trip']
        extra_kwargs = {
            'status': {'read_only': True},
        }

    def validate(self, attrs):
        return attrs
    """def create(self,request,  validated_data):
        client = validated_data.get_or_create(request.user.id)
        ressrvation = Reservations.objects.get_or_create(client=client)
        ressrvation.save()
        return ressrvation"""



class ReviewSerializer(serializers.ModelSerializer):
    trip = serializers.PrimaryKeyRelatedField(queryset=Trip.objects.only('id'))
    class Meta:
        model = Reviews
        fields = ['id', 'trip', 'rate', 'feedback', 'created_at']


    def validate(self, attrs):
        return attrs



class GettingReviewSerializer(serializers.ModelSerializer):
    trip = TripSerializerMultiLanguage()
    class Meta:
        model = Reviews
        fields = ['id', 'rate', 'feedback', 'created_at', 'trip']



class AddFavoriteSerializer(serializers.ModelSerializer):
    favs = serializers.PrimaryKeyRelatedField(queryset=Trip.objects.only('id'))
    class Meta:
        model = Favorites
        fields = ['id', 'favs']

    def validate(self, attrs):
        return attrs



class ReadFavoriteSerializer(serializers.ModelSerializer):
    favs = TripSerializerMultiLanguage()
    class Meta:
        model = Favorites
        fields = ['id', 'favs']



