from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # автоматичний вхід після реєстрації
            messages.success(request, 'Реєстрація успішна! Ласкаво просимо!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def user_logout(request):
    print('вихід вдалий')
    logout(request)
    return render(request, 'users/logout.html') 

@login_required
def profile(request):
    return render(request, 'users/profile.html')