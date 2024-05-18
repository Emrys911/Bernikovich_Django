from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.db import transaction
from myapp import Reservation

from models import Comment
from .models import Hotel, Room, Booking, User, Comment
from django import forms
from django.db.models import Q, QuerySet


@login_required
def view_profile(request):
    return render(request, 'base.html')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'  # Используйте '__all__' для включения всех полей

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def is_valid(self):
        return super().is_valid()


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels': hotels})


def hotel_list(request):
    hotels = Hotel.objects.prefetch_related('owner', 'comments').all()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})


def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def user_list(request):
    users = User.objects.prefetch_related('hobbies').all()
    return render(request, 'users.html', {'users': users})


def comments(request):
    comments: QuerySet[Comment] = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})


def get(request, hotel_name, user_id, room_number):
    # Получаем информацию о пользователе и отеле
    hotel = get_object_or_404(Hotel, name=hotel_name)
    user = get_object_or_404(User, id=user_id)
    room = get_object_or_404(Room, number=room_number, hotel=hotel)

    # Проверяем, не забронирована ли уже комната
    if room.is_booked:
        return JsonResponse({'error': 'Эта комната уже забронирована.'}, status=400)

    # Транзакционно бронируем комнату
    with transaction.atomic():
        room.is_booked = True
        room.save()
        # Создаем объект бронирования
        booking = Booking.objects.create(
            room=room,
            start_date=request.GET.get('start_date'),
            end_date=request.GET.get('end_date'),
            customer_full_name=user.full_name
        )
    return JsonResponse({'success': 'Комната успешно забронирована.'})


class BookRoomView(View):
    def post(self, request, hotel_name, room_number, start_date, end_date):
        room = Room.objects.filter(
            hotel__name=hotel_name,
            number=room_number,
            bookings__isnull=True | ~Q(bookings__start_date__lte=end_date, bookings__end_date__gte=start_date)
        ).first()

        if room:
            try:
                with transaction.atomic():
                    Booking.objects.create(
                        room=room,
                        start_date=start_date,
                        end_date=end_date,
                        customer_full_name=request.POST.get('customer_full_name')
                    )
                    room.is_booked = True
                    room.save()
                    return JsonResponse({'success': 'Комната успешно забронирована.'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        return JsonResponse({'error': 'Комната не доступна для бронирования на указанные даты.'}, status=400)


class CheckAndBookRoomView(View):
    def post(self, request, hotel_name, room_number, start_date, end_date):
        room = Room.objects.filter(
            hotel__name=hotel_name,
            number=room_number,
            bookings__isnull=True | ~Q(bookings__start_date__lte=end_date, bookings__end_date__gte=start_date)
        ).first()

        if room:
            try:
                with transaction.atomic():
                    Booking.objects.create(
                        room=room,
                        start_date=start_date,
                        end_date=end_date,
                        customer_full_name=request.POST.get('customer_full_name')
                    )
                    room.is_booked = True
                    room.save()
                    return JsonResponse({'success': 'Комната успешно забронирована.'})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Комната не доступна для бронирования на указанные даты.'}, status=400)


def cancel_reservation(request, reservation_id):
    try:
        with transaction.atomic():
            reservation = Reservation.objects.select_for_update().get(id=reservation_id)
            if reservation:
                reservation.status = 'cancelled'
                reservation.save()
            else:
                return JsonResponse({'error': f'Бронирование с ID {reservation_id} не найдено.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Произошла ошибка при отмене бронирования: {e}'}, status=500)
    return JsonResponse({'success': f'Бронирование с ID {reservation_id} успешно отменено.'})
