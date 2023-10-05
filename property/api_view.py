from django.db.migrations import serializer
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Trip, Category, Place, PropertyAvailabilityCheck, Visa, Reservations, Reviews, Favorites
from .serializers import TripSerializerMultiLanguage, PropertyDetailSerializer, CategorySerializer, \
    CategoryListSerializer, PlaceListSerializer, PlaceSerializer, TripGallerySerializer, \
    PropertyAvailabilityCheckSerializer, VisaSerializer, VisaUserSerializer, ReservationsSerializer, \
    GettingReservationsSerializer, ReviewSerializer, GettingReviewSerializer, AddFavoriteSerializer \
    , ReadFavoriteSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import AccountPorfileSerializer
from accounts.accounts_serializer import Account, AccountSerializer




class PropertyApiList(ListAPIView):
    queryset = Trip.objects.language('en-us').only('translations',
                                                   'stars',
                                                   'price_of_single_room_by_person_night',
                                                   'price_of_double_room_by_person_night',
                                                   'price_of_triple_room_by_person_night',
                                                   'price_of_single_room_by_night',
                                                   'price_of_double_room_by_night',
                                                   'price_of_triple_room_by_night',
                                                   'image',
                                                   'place',
                                                   'image',
                                                   'category')
    serializer_class = TripSerializerMultiLanguage

class PropertyApiListAr(ListAPIView):
    queryset = Trip.objects.language('ar-sa').only('translations',
                                                   'stars',
                                                   'price_of_single_room_by_person_night',
                                                   'price_of_double_room_by_person_night',
                                                   'price_of_triple_room_by_person_night',
                                                   'price_of_single_room_by_night',
                                                   'price_of_double_room_by_night',
                                                   'price_of_triple_room_by_night',
                                                   'image',
                                                   'place',
                                                   'image',
                                                   'category')
    serializer_class = TripSerializerMultiLanguage



class PropertyApiDetail(RetrieveAPIView):
    queryset = Trip.objects.language('en-us').only('translations',
                                                   'stars',
                                                   'price_of_single_room_by_person_night',
                                                   'price_of_double_room_by_person_night',
                                                   'price_of_triple_room_by_person_night',
                                                   'price_of_single_room_by_night',
                                                   'price_of_double_room_by_night',
                                                   'price_of_triple_room_by_night',
                                                   'image',
                                                   'place',
                                                   'image',
                                                   'category',
                                                   'created_at',
                                                   'number_of_guests',
                                                   'number_of_rooms',
                                                   'duration',
                                                   'price_per_child',
                                                   'check_in',
                                                   'check_out')
    serializer_class = PropertyDetailSerializer



class PropertyApiDetailAR(RetrieveAPIView):
    queryset = Trip.objects.language('ar-sa').only('translations',
                                                   'stars',
                                                   'price_of_single_room_by_person_night',
                                                   'price_of_double_room_by_person_night',
                                                   'price_of_triple_room_by_person_night',
                                                   'price_of_single_room_by_night',
                                                   'price_of_double_room_by_night',
                                                   'price_of_triple_room_by_night',
                                                   'image',
                                                   'place',
                                                   'image',
                                                   'category',
                                                   'created_at',
                                                   'number_of_guests',
                                                   'number_of_rooms',
                                                   'duration',
                                                   'price_per_child',
                                                   'check_in',
                                                   'check_out')
    serializer_class = PropertyDetailSerializer



"""def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
        myform = form.save(commit=False)
        myform.property = self.get_object()
        myform.user = request.user
        myform.save()"""

class Categories(ListAPIView):
    queryset = Category.objects.language('en-us').only('translations')
    serializer_class = CategoryListSerializer

class CategoriesAR(ListAPIView):
    queryset = Category.objects.language('ar-sa').only('translations')
    serializer_class = CategoryListSerializer


class Places(ListAPIView):
    queryset = Place.objects.language('en-us').only('translations', 'image')
    serializer_class = PlaceListSerializer


class PlacesAR(ListAPIView):
    queryset = Place.objects.language('ar-sa').only('translations', 'image')
    serializer_class = PlaceListSerializer



class TripsByFilters(ListAPIView):
    queryset = Trip.objects.language('en-us').only('translations',
                                                   'stars',
                                                   'price_of_single_room_by_person_night',
                                                   'price_of_double_room_by_person_night',
                                                   'price_of_triple_room_by_person_night',
                                                   'price_of_single_room_by_night',
                                                   'price_of_double_room_by_night',
                                                   'price_of_triple_room_by_night',
                                                   'image',
                                                   'place',
                                                   'image',
                                                   'category')
    serializer_class = TripSerializerMultiLanguage

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        by_category = Trip.objects.language('en-us').filter(
            Q(category__translations__title__icontains=slug)
        )
        by_place = Trip.objects.language('en-us').filter(
            Q(place__translations__title__icontains=slug)
        )
        by_trips_name_and_description = Trip.objects.language('en-us').filter(
            Q(translations__title__icontains=slug) |
            Q(translations__description__icontains=slug)
        )
        by_trip_check_in_date = Trip.objects.language('en-us').filter(
            Q(check_in__icontains=slug)
        )

        data = TripSerializerMultiLanguage(by_category, many=True, context={'request': request}).data
        data2 = TripSerializerMultiLanguage(by_place, many=True, context={'request': request}).data
        data3 = TripSerializerMultiLanguage(by_trips_name_and_description, many=True, context={'request': request}).data
        data4 = TripSerializerMultiLanguage(by_trip_check_in_date, many=True, context={'request': request}).data

        return Response({'by category':data,
                         'by place':data2,
                         'by trip name or description':data3,
                         'by trip check in data':data4})




class TripsByFiltersAR(ListAPIView):
    queryset = Trip.objects.language('ar-sa').only('translations',
                                                   'stars',
                                                   'price_of_single_room_by_person_night',
                                                   'price_of_double_room_by_person_night',
                                                   'price_of_triple_room_by_person_night',
                                                   'price_of_single_room_by_night',
                                                   'price_of_double_room_by_night',
                                                   'price_of_triple_room_by_night',
                                                   'image',
                                                   'place',
                                                   'image',
                                                   'category')
    serializer_class = TripSerializerMultiLanguage

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        by_category = Trip.objects.language('ar-sa').filter(
            Q(category__translations__title__icontains=slug)
        )
        by_place = Trip.objects.language('ar-sa').filter(
            Q(place__translations__title__icontains=slug)
        )
        by_trips_name_and_description = Trip.objects.language('ar-sa').filter(
            Q(translations__title__icontains=slug) |
            Q(translations__description__icontains=slug)
        )
        by_trip_check_in_date = Trip.objects.language('ar-sa').filter(
            Q(check_in__icontains=slug)
        )

        data = TripSerializerMultiLanguage(by_category, many=True, context={'request': request}).data
        data2 = TripSerializerMultiLanguage(by_place, many=True, context={'request': request}).data
        data3 = TripSerializerMultiLanguage(by_trips_name_and_description, many=True, context={'request': request}).data
        data4 = TripSerializerMultiLanguage(by_trip_check_in_date, many=True, context={'request': request}).data

        return Response({'by category':data,
                         'by place':data2,
                         'by trip name or description':data3,
                         'by trip check in data':data4})


"""class PropertyByPlace(ListAPIView):
    queryset = Trip.objects.only('id', 'title', 'image', 'price_of_double_room_by_night', 'place', 'category')
    serializer_class = TripSerializerMultiLanguage

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        list = Trip.objects.filter(
            Q(place__title__icontains=slug)
        )
        data = TripSerializerMultiLanguage(list, many=True, context={'request': request}).data
        return Response({'data':data})"""


class Inquiry(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = AccountPorfileSerializer(request.user, context={'request':request})
        return Response({'inquiry_owner':serializer.data})
    def post(self, request, format=None):
        inquiry_serializer = PropertyAvailabilityCheckSerializer(data=request.data)
        if inquiry_serializer.is_valid():
            inquiry_serializer2 = inquiry_serializer.save()
            return Response({'msg':'We have received your inquiry successfully & we will reply to you as soon as possible',
                             'inquiry':PropertyAvailabilityCheckSerializer(inquiry_serializer2).data, 'inquiry_owner':AccountPorfileSerializer(request.user, context={'request':request}).data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





"""class Inquiry(CreateAPIView):
    queryset = PropertyAvailabilityCheck.objects.only()
    serializer_class = PropertyAvailabilityCheckSerializer"""


"""class Inquiry(APIView):
    def post(self, request, format=None):
        serializer = PropertyAvailabilityCheckSerializer(data=request.data)
        if serializer.is_valid():
            inquery = serializer.save()
            return Response({'msg':'We have received your inquery successfully & we will reply to you as soon as possible',
                             'inquery':inquery}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

"""class VisaSubmit(CreateAPIView):
    queryset = Visa.objects.only('user', 'visa', 'photo')
    serializer_class = VisaSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = AccountSerializer(request.user, context={'request':request})
        return Response({'data':serializer.data})"""


class VisaSubmit(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = AccountPorfileSerializer(request.user, context={'request': request})
        return Response({'visa_owner':serializer.data})
    def post(self, request, format=None):
        visa_serializer = VisaSerializer(data=request.data, context={'request': request})
        if visa_serializer.is_valid():
            visa_serilaizer2 = visa_serializer.save()
            return Response({'msg':'We have received your visa successfully & we will reply to you as soon as possible',
                             'visa':VisaSerializer(visa_serilaizer2).data, 'visa owner':AccountPorfileSerializer(request.user).data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Reservation(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, format=None):
        get_object_or_404(Trip, pk=pk)
        reservation_serializer = ReservationsSerializer(data=request.data)
        if reservation_serializer.is_valid():
            reservation_serializer2 = reservation_serializer.save(client=request.user)
            return Response({'msg':'We have received your reservation successfully & we will reply to you as soon as possible',
                             'reservation':ReservationsSerializer(reservation_serializer2).data,
                             'reservation owner':AccountPorfileSerializer(request.user).data},
                             status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


"""@api_view(['POST'])
def reservation(self, request, pk, format=None):
    reservations = get_object_or_404(Reservations, pk=pk)
    reservations.delete(client=request.user)"""



"""class Reservation(CreateAPIView):
    queryset = Reservations.objects.only('status',
                                         'client',
                                         'trip',
                                         'adult_number',
                                         'guests_info',
                                         'children_number_and_their_age',
                                         'infant',
                                         'notes',
                                         'created_at')
    serializer_class = ReservationsSerializer
    permission_classes = [IsAuthenticated]"""



class Review(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, format=None):
        get_object_or_404(Trip, pk=pk)
        review_serializer = ReviewSerializer(data=request.data)
        if review_serializer.is_valid():
            review_serializer2 = review_serializer.save(client=request.user)
            return Response({'msg':'you have submitted your review successfully',
                             'review':ReviewSerializer(review_serializer2).data,
                             'reviewer':AccountPorfileSerializer(request.user).data},
                             status=status.HTTP_202_ACCEPTED)
        else:
            return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddFavorite(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, format=None):
        get_object_or_404(Favorites, pk=pk)
        favorite_serializer = AddFavoriteSerializer(data=request.data)
        if favorite_serializer.is_valid():
            favorite_serializer2 = favorite_serializer.save(client=request.user)
            return Response({'msg':'you have added this trip to your favorites successfully',
                             'favorite':AddFavoriteSerializer(favorite_serializer2).data,
                             'favorite owner':AccountPorfileSerializer(request.user).data},
                             status=status.HTTP_202_ACCEPTED)
        else:
            return Response(favorite_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




"""class AddFavorite(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, format=None):
        favs = get_object_or_404(Favorites, pk=pk)
        favs.save(request.user)
        return Response(status=status.HTTP_200_OK)"""



class Dashboard(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        reservations = Reservations.objects.filter(client=request.user)
        reservations_serializer = GettingReservationsSerializer(reservations, many=True, context={'request': request})
        reviews = Reviews.objects.filter(client=request.user)
        reviews_serializer = GettingReviewSerializer(reviews, many=True, context={'request': request})
        favs = Favorites.objects.filter(client=request.user)
        favs_serializer = ReadFavoriteSerializer(favs, many=True, context={'request': request})
        return Response({'reservations':reservations_serializer.data,
                         'reviews':reviews_serializer.data,
                         'favs':favs_serializer.data,
                         'user':AccountPorfileSerializer(request.user, context={'request': request}).data})
@api_view(['DELETE'])
def delete_reservations(request, pk):
    if request.user.is_authenticated:
        reservations = get_object_or_404(Reservations, pk=pk)
        reservations.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
def delete_review(request, pk):
    if request.user.is_authenticated:
        reviews = get_object_or_404(Reviews, pk=pk)
        reviews.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
def delete_favorite(request, pk):
    if request.user.is_authenticated:
        favs = get_object_or_404(Favorites, pk=pk)
        favs.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)







"""class DeleteReservation(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        reservation = get_object_or_404(Reservations, pk=pk)
        reservation.delete()
        return Response(status=status.HTTP_200_OK)"""


"""def delete(self, request, pk, format=None):
    reservation = get_object_or_404(Reservations, pk=pk)
    reservation.delete()
    return Response(status=status.HTTP_200_OK)"""






