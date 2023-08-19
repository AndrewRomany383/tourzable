from django.db.models import Q
from .models import Property, Category, Place, PropertyAvailabilityCheck, Visa
from .forms import PropertyBookForm
from .serializers import PropertySerializer, PropertyDetailSerializer,CategorySerializer, PlaceSerializer, PropertyImagesSerializer, PropertyAvailabilityCheckSerializer, VisaSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response




class PropertyApiList(ListAPIView):
    queryset = Property.objects.only('name', 'image', 'price_of_double_room_by_night', 'place')
    serializer_class = PropertySerializer


class PropertyApiDetail(RetrieveAPIView):
    queryset = Property.objects.only('name', 'image', 'price_of_double_room_by_night', 'description', 'place', 'created_at','slug')
    serializer_class = PropertyDetailSerializer



"""def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
        myform = form.save(commit=False)
        myform.property = self.get_object()
        myform.user = request.user
        myform.save()"""

class Categories(ListAPIView):
    queryset = Category.objects.only('name')
    serializer_class = CategorySerializer

class PropertyByCategory(ListAPIView):
    queryset = Property.objects.only('name', 'image', 'price_of_double_room_by_night', 'place')
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        object_list = Property.objects.filter(
            Q(category__name__icontains=slug)
        )
        data = PropertySerializer(object_list, many=True, context={'request':request}).data
        return Response({'data':data})

class Places(ListAPIView):
    queryset = Place.objects.only('name', 'image')
    serializer_class = PlaceSerializer

class PropertyByPlace(ListAPIView):
    queryset = Property.objects.only('name', 'image', 'price_of_double_room_by_night', 'place', 'category')
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        list = Property.objects.filter(
            Q(place__name__icontains=slug)
        )
        data = PropertySerializer(list, many=True, context={'request':request}).data
        return Response({'data':data})


class Inquiry(CreateAPIView):
    queryset = PropertyAvailabilityCheck.objects.only()
    serializer_class = PropertyAvailabilityCheckSerializer


"""class Inquiry(APIView):
    def post(self, request, format=None):
        serializer = PropertyAvailabilityCheckSerializer(data=request.data)
        if serializer.is_valid():
            inquery = serializer.save()
            return Response({'msg':'We have received your inquery successfully & we will reply to you as soon as possible',
                             'inquery':inquery}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

class VisaSubmit(CreateAPIView):
    queryset = Visa.objects.only('username', 'email', 'phone_number', 'visa', 'photo')
    serializer_class = VisaSerializer
    permission_classes = [IsAuthenticated]

"""class VisaSubmit(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = VisaSerializer(data=request.data)
        if serializer.is_valid():
            visa = serializer.save()
            return Response({'msg':'We have received your inquery successfully & we will reply to you as soon as possible',
                             'visa':visa}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

























