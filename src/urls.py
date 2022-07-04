from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import VenueViewSet

router = DefaultRouter()
router.register(r"venues", VenueViewSet, basename="venues")

urlpatterns = [
    path("", include(router.urls)),
    # path("", VenueView.as_view(), name="venue"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
