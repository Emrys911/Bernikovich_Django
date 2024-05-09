from django import forms
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Дополнительные поля профиля


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


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['age', 'photo']


class Hotel(models.Model):
    name = models.CharField(max_length=40)
    stars = models.IntegerField()
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.name


# Создание объектов и запросы к базе данных
def create_objects_and_queries():
    # Создание объектов для модели User
    user1 = User.objects.create(name="Alice", age=25)
    user2 = User.objects.create(name="Bob", age=35)
    user3 = User.objects.create(name="Charlie", age=40)

    # Создание объектов для модели Hotel
    hotel_bnb = Hotel.objects.create(name="B&B", rating=5)

    # Привязка хобби к пользователям
    hobby1 = Hobby.objects.create(name="Reading")
    hobby2 = Hobby.objects.create(name="Cooking")
    hobby3 = Hobby.objects.create(name="Traveling")
    user1.hobby.add(hobby1, hobby2)
    user2.hobby.add(hobby2, hobby3)
    user3.hobby.add(hobby1, hobby3)

    # Создание объектов для модели Establishment
    establishment_a = Establishment.objects.create(name="Restaurant A", hotel=hotel_bnb)
    establishment_b = Establishment.objects.create(name="Spa B", hotel=hotel_bnb)

    # Создание объектов для модели Comment
    Comment.objects.create(content="Great hotel!", user=user1, hotel=hotel_bnb, establishment=establishment_a)
    Comment.objects.create(content="Amazing service!", user=user2, hotel=hotel_bnb, establishment=establishment_b)

    # Запросы к базе данных
    users_over_30_in_bnb = User.objects.filter(age__gt=30, profile__hotel__name="B&B")
    girls_with_many_hobbies = User.objects.filter(profile__gender="female", hobby__count__gt=3)[:5]
    top_establishments = Establishment.objects.filter(hotel__rating=5)
    comments_bnb_20_to_30 = Comment.objects.filter(hotel__name="B&B", user__age__range=(20, 30))
    bb_owner_profile: Profile = Profile.objects.get(user__hotel__name="B&B", is_owner=True)

    return users_over_30_in_bnb, girls_with_many_hobbies, top_establishments, comments_bnb_20_to_30, bb_owner_profile
