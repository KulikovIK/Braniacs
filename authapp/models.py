from django.db import models
from django.contrib.auth.models import AbstractUser
from mainapp.models import NULLABLE


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', blank=True, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', **NULLABLE)
    avatar = models.ImageField(
        verbose_name='аватар', upload_to='users', **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return f'{self.pk} | {self.username}'
