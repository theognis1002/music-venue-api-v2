from django.urls import path, include
from .views import VenueView, test_route


urlpatterns = [
    path('', VenueView.as_view(), name='venue'),
    path('test_route/', test_route, name='test route'),
]
