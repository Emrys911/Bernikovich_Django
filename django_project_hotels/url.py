import views
from django.urls import path
from views import BookRoomView
from django.urls import path
from views import HomePageView, AboutPageView, ContactPageView


urlpatterns = [
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('', views.index, name='index'),  # Главная страница
    path('hotels/', views.hotels, name='hotels'),  # Страница с отелями
    path('users/', views.users, name='users'),  # Страница с пользователями
    path('comments/', views.comments, name='comments'),  # Страница с комментариями
    path('book-room/<str:hotel_name>/<int:user_id>/<str:room_number>/', BookRoomView.as_view(), name='book-room'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

]
