from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Venue
from .serializers import VenueSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    authentication_classes = []
    permission_classes = []
