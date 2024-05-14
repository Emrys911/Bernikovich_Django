from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms


# Объединенный класс User с полями из обоих определений
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])

# Остальные классы моделей
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

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


