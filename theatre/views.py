from rest_framework import viewsets, mixins
from .serializers import *

class PlayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

class PerformanceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

class TheatreHallViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer

class ReservationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
