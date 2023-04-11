from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import check_birth_date, check_email


class Location(models.Model):
    name = models.CharField(verbose_name='Название', max_length=300)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(AbstractUser):
    ROLES = [
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
        ('member', 'Пользователь'),
    ]

    role = models.CharField(max_length=20, choices=ROLES, default='member')
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date])
    email = models.EmailField(unique=True, null=True, validators=[check_email])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
