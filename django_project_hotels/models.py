from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms


# Объединенный класс User с полями из обоих определений
class User(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.full_name = None

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])


# Остальные классы моделей
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Hobby(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)


# Форма для модели User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'age']


class BaseHotelModel(models.Model):
    # Общие поля, которые будут использоваться в других моделях
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Hotels(BaseHotelModel):
    name = models.CharField(max_length=255)
    address = models.TextField()


class Room(BaseHotelModel):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)
    # Другие поля...


class Booking(BaseHotelModel):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_full_name = models.CharField(max_length=255)
