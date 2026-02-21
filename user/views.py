from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, CustomAuthForm
from . import models
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView



class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = CustomUserForm


    def get_success_url(self):
        return reverse('login')
   
    

#def register_view(request):
#    if request.method == 'POST':
#        form = CustomUserForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect("/login/")
#    else:
#        form = CustomUserForm()
#    return render(
#        request, 
#        'register.html', 
#        {
#            "form": form
#        }
#    )



class AuthLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthForm

    def get_success_url(self):
        return reverse('profile')



#def auth_login_view(request):
#    if request.method == 'POST':
#        form = CustomAuthForm(data=request.POST)
#        if form.is_valid():
#            user = form.get_user()
#            login(request, user)
#            return redirect('/profile/')
#    else:
#        form = CustomAuthForm()
#    return render(
#        request,
#        'login.html', 
#        {
#            "form": form
#        }
#    )


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('login')


#def auth_logout_view(request):
#    logout(request)
#    return redirect('/login/')



class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'profile.html'
    context_object_name = 'custom_user'
    model = models.CustomUser
    
    def get_object(self, queryset=None):
        return models.CustomUser.objects.get(user_ptr_id=self.request.user.id)

#@login_required
#def profile_view(request):
#    custom_user = models.CustomUser.objects.get(id=request.user.id)
#    return render(
#        request, 
#        'profile.html', 
#        {
#            "custom_user": custom_user
#        }
#    )

