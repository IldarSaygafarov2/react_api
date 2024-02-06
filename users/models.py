from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(verbose_name='Фото пользователя', null=True, blank=True, upload_to='users/avatars/')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
