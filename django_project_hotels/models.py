from aiogram.types import User
from django import forms
from django.db import models

class Models:
    pass

class UserProfile:
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='user_photos', blank=True, null=True)

    class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ['age', 'photo']


class Person(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=40)
    stars = models.IntegerField()
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.name


