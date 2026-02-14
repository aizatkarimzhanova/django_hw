from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField 

GENDER = (
    ('MALE', 'Мужской'),
    ('FEMALE', 'Женский'),
)

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Электронная почта')
    photo = forms.ImageField(required=True, label='Фото')
    phone_number = forms.CharField(max_length=20, initial='+996', required=True, label='Номер телефона')
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Пол')
    city = forms.CharField(max_length=100, required=True, label='Город')
    birthday = forms.DateField(required=True, label='Дата рождения', widget=forms.DateInput(attrs={'type':'date'}))
    education = forms.CharField(max_length=100, required=False, label='Образование')
    experience = forms.CharField(widget=forms.Textarea, required=False, label='Опыт работы')
    skills = forms.CharField(widget=forms.Textarea, required=False, label='Навыки')

    class Meta:
        model = CustomUser
        fields = (
                'username',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'email', 
                  'photo', 
                  'phone_number', 
                  'gender', 
                  'city', 
                  'birthday',
                  'education', 
                  'experience', 
                  'skills'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
   
        if commit:
            user.save()
        return user



class CustomAuthForm(AuthenticationForm):
    captcha = CaptchaField(label='Введите символы с картинки')  