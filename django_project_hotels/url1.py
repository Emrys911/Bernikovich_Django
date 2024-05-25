from django.urls import path
from views import CheckAndBookRoomView
from django.urls import path
from views import YourModelDetailView, YourModelListView

urlpatterns = [
    # URL для проверки и бронирования комнаты
    path('check-and-book-room/<str:hotel_name>/<str:room_number>/<str:start_date>/<str:end_date>/', CheckAndBookRoomView.as_view(), name='check_and_book_room'),
    path('yourmodel/<int:pk>/', YourModelDetailView.as_view(), name='yourmodel_detail'),
    path('yourmodel/', YourModelListView.as_view(), name='yourmodel_list'),
]
