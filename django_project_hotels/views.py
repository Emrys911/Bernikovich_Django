from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django import forms
from .models import User, Hotel, Comment

@login_required
def view_profile(request):
    return render(request, 'base.html')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'all'  # Исправлено на 'all'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

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
    return render(request, 'users/user_list.html', {'users': users})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})
