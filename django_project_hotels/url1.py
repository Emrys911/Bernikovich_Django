from django.urls import path
from .views import CheckAndBookRoomView

urlpatterns = [
    # URL для проверки и бронирования комнаты
    path('check-and-book-room/<str:hotel_name>/<str:room_number>/<str:start_date>/<str:end_date>/', CheckAndBookRoomView.as_view(), name='check_and_book_room'),
]