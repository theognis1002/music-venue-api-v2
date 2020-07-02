from django.shortcuts import render
from django.http import JsonResponse

from .serializers import VenueSerializer

from rest_framework import views, generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .models import Venue



class VenueView(views.APIView):
    """api class endpoint"""
    def get(self, request, *args, **kwargs):
        qs = Venue.objects.all()
        serializer = VenueSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class VenueList(generics.ListCreateAPIView):
    """api class endpoint"""
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    # permission_classes = [IsAdminUser]


# basic authentication = username/pw
# sessionauthentication = logged in
# token authentication = API/token
class VenueModelViewSet(viewsets.ModelViewSet):
    """Model Viewset (easy mode - inherits get/post/put/delete methods)"""
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    authentication_classes = [TokenAuthentication]
    # authentication_classes  = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def GetVenueList(request):
    """api decorator endpoint - retrieve all venues in database"""
    qs = Venue.objects.all()
    serializer = VenueSerializer(qs, many=True) # many=True for .all() queryset method
    return Response(serializer.data)


@api_view(['GET'])
def VenueDetail(request, pk):
    """api decorator endpoint - retrieve single venue based on primary id"""
    qs = Venue.objects.get(id=pk)
    serializer = VenueSerializer(qs, many=False)  # many=False for .get() queryset method, many=True for .filter() queryset method
    return Response(serializer.data)


@api_view(['POST'])
def CreateVenue(request):
    """api decorator endpoint - post single venue """
    serializer = VenueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def UpdateVenue(request, pk):
    """api decorator endpoint - post single venue """
    old_venue_data = Venue.objects.get(id=pk)
    serializer = VenueSerializer(instance=old_venue_data, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteVenue(request, pk):
    """api decorator endpoint - post single venue """
    venue = Venue.objects.get(id=pk)
    venue.delete()

    return Response("Item deleted")