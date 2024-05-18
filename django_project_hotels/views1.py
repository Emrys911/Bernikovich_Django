from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from django.db import transaction
from .models import Room, Booking


class CheckAndBookRoomView(View):
    def post(self, request, hotel_name, room_number, start_date, end_date):
        # Проверяем, существует ли комната и не забронирована ли она на указанные даты
        room = Room.objects.filter(
            hotel__name=hotel_name,
            number=room_number,
            bookingsisnull=True | ~Q(bookingsstart_datelte=end_date, bookingsend_date__gte=start_date)
        ).first()

        if room:
            # Комната свободна, пытаемся забронировать
            try:
                with transaction.atomic():
                    # Создаем объект бронирования
                    booking = Booking.objects.create(
                        room=room,
                        start_date=start_date,
                        end_date=end_date,
                        customer_full_name=request.POST.get('customer_full_name')
                    )
                    room.is_booked = True
                    room.save()
                    return JsonResponse({'success': 'Комната успешно забронирована.'})
            except Exception as e:
                # В случае ошибки возвращаем сообщение об ошибке
                return JsonResponse({'error': str(e)}, status=500)
        else:
            # Комната не найдена или уже забронирована
            return JsonResponse({'error': 'Комната не доступна для бронирования на указанные даты.'}, status=400)
