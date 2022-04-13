from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField('Имя пользователя', max_length=75, unique=True)
    firstname = models.CharField('Имя', max_length=75, blank=True)
    lastname = models.CharField('Фамилия', max_length=75, blank=True)
    email = models.EmailField(verbose_name='Электронный адрес', max_length=254, unique=True)
