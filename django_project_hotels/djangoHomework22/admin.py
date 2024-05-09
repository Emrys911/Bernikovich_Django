from django.contrib import admin

from models import Hotel, User, Comment, Establishment, Hobby, Profile


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Hobby)
admin.site.register(Hotel)
admin.site.register(Establishment)
admin.site.register(Comment)
user1 = User.objects.create(name="Alice", age=25)
user2 = User.objects.create(name="Bob", age=35)
hotel = Hotel.objects.create(name="B&B")