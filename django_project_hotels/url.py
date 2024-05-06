from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
 path('', views.index, name='index'),  # Главная страница
    path('hotels/', views.hotels, name='hotels'),  # Страница с отелями
    path('users/', views.users, name='users'),  # Страница с пользователями
    path('comments/', views.comments, name='comments'),  # Страница с комментариями
]
