from django_filters import rest_framework as filters
from .models import Property
from .serializers import PropertySerializer
from rest_framework import generics



class PropertyFilter(filters.FilterSet):
    class Meta:
        model = Property
        fields = ['name', 'description', 'place', 'category']



class PropertyList(generics.ListAPIView):
    queryset = Property.objects.only('name', 'description', 'place', 'category')
    serializer_class = PropertySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PropertyFilter


























