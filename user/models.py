from django.db import models

from django.contrib.auth.models import User

class CustomUser(User):
    photo = models.ImageField(upload_to='resume_users/', null=True, blank=True, verbose_name='Фото' )
    phone_number = models.CharField(max_length=20, default='+996', verbose_name='Номер телефона')
    GENDER = (
        ('MALE', 'Мужской'),
        ('FEMALE', 'Женский'),
    )
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE', verbose_name='Пол')
    city = models.CharField(max_length=100, default='Бишкек', verbose_name='Город')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    education = models.CharField(max_length=200, blank=True, verbose_name='Образование')
    experience = models.TextField(verbose_name='Опыт работы')
    skills = models.TextField(verbose_name='Навыки')

    def __str__(self):
        return self.username