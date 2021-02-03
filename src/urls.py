from django.conf.urls import url
from django.urls import path, include
from .views import VenueView, GetVenueList, VenueList, VenueDetail, CreateVenue, UpdateVenue, DeleteVenue, VenueModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'venues', VenueModelViewSet, basename='venues')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('', VenueView.as_view(), name='venue'),
    path('venuelist/', VenueList.as_view(), name='venuelist'),
    path('test_route/', GetVenueList, name='venuelist'),
    path('venue_detail/<str:pk>/', VenueDetail, name='venuedetail'),
    path('venue_create/', CreateVenue, name='createvenue'),
    path('venue_update/<str:pk>/', UpdateVenue, name='updatevenue'),
    path('venue_delete/<str:pk>/', DeleteVenue, name='updatevenue'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
