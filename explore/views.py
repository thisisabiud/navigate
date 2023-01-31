from rest_framework import generics

from .models import Place

from .serializers import PlaceSerializer


class PlaceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    lookup_field = 'name'