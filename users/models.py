from django.db import models


class Location(models.Model):
    name = models.CharField(verbose_name='Название', max_length=300)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class UserRoles(models.TextChoices):
    MEMBER = 'member', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'


class User(models.Model):
    # ROLES = [
    #     ('admin', 'Администратор'),
    #     ('moderator', 'Модератор'),
    #     ('member', 'Пользователь'),
    # ]

    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    # role = models.CharField(max_length=20, choices=ROLES, default='member')
    role = models.CharField(choices=UserRoles.choices, max_length=9)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
