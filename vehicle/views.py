from rest_framework import viewsets, generics
from vehicle.models import Car, Bike
from vehicle.serializers import CarSerializer, BikeSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class BikeCreateAPIView(generics.CreateAPIView):
    serializer_class = BikeSerializer


class BikeListAPIView(generics.ListAPIView):
    serializer_class = BikeSerializer
    queryset = Bike.objects.all()


class BikeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BikeSerializer
    queryset = Bike.objects.all()


class BikeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BikeSerializer
    queryset = Bike.objects.all()


class BikeDestroyAPIView(generics.DestroyAPIView):
    queryset = Bike.objects.all()