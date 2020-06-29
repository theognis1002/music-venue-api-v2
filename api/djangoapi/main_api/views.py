from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import Venue
from .serializers import VenueSerializer


class VenueView(views.APIView):
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