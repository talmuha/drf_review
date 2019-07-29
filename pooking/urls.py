from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from hotels.views import (
    HotelList,
    BookingList,
    BookingDetail,
    BookingDelete,
    BookingUpdate,
    BookingCreate,
    Register,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hotels/', HotelList.as_view(), name="api-hotel-list"),
    path('api/bookings/', BookingList.as_view(), name="api-booking-list"),
    path('api/bookings/<int:book_id>/', BookingDetail.as_view(), name="api-booking-detail"),
    path('api/bookings/<int:book_id>/delete/', BookingDelete.as_view(), name="api-booking-delete"),
    path('api/bookings/<int:book_id>/update/', BookingUpdate.as_view(), name="api-booking-update"),
    path('api/book/<int:hotel_id>/create/', BookingCreate.as_view(), name="api-booking-update"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', Register.as_view(), name="api-register"),
]
