from tokenize import Comment

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from models import Hotel, User


@login_required
def view_profile(request):
    return render(request, 'users.html')


class UserForm:
    def save(self):
        pass

    def is_valid(self):
        pass


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user.userprofile)  # Подстановка правильной формы
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm(instance=request.user.userprofile)  # Использование правильной формы
    return render(request, 'edit_profile.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels': hotels})


def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def comments(request):
    # Возможно, имелось в виду что-то другое, чем просто загрузка пользователей.
    # Если это комментарии, то вероятно, надо получить комментарии, а не пользователей.
    comments = Comment.objects.all()  # Предположим, что у вас есть модель Comment
    return render(request, 'comments.html', {'comments': comments})
