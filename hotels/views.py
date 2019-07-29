
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from .models import Hotel, Booking
from .serializers import HotelSerializer, BookingSerializer, BookingUpdateSerializer, RegisterSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import Booker, BackToTheFuture

import datetime


class HotelList(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [AllowAny,]

class BookingList(ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        today = datetime.date.today()
        return Booking.objects.filter(check_in__gte=today, user=self.request.user)


class BookingDetail(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
    permission_classes = [IsAuthenticated, Booker, ]

class BookingDelete(DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
    permission_classes = [IsAuthenticated, Booker, BackToTheFuture]


class BookingUpdate(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
    permission_classes = [IsAuthenticated, Booker, BackToTheFuture]

class BookingCreate(CreateAPIView):
    serializer_class = BookingUpdateSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,hotel_id=self.kwargs['hotel_id'])


class Register(CreateAPIView):
    serializer_class = RegisterSerializer
