from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    PlayViewSet,
    PerformanceViewSet,
    TheatreHallViewSet,
    ReservationViewSet
)

router = DefaultRouter()
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)
router.register("theatres", TheatreHallViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
