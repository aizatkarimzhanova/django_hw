from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, CustomAuthForm
from . import models

def register_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = CustomUserForm()
    return render(
        request, 
        'register.html', 
        {
            "form": form
        }
    )



def auth_login_view(request):
    if request.method == 'POST':
        form = CustomAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/profile/')
    else:
        form = CustomAuthForm()
    return render(
        request,
        'login.html', 
        {
            "form": form
        }
    )



def auth_logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def profile_view(request):
    custom_user = models.CustomUser.objects.get(id=request.user.id)
    return render(
        request, 
        'profile.html', 
        {
            "custom_user": custom_user
        }
    )
