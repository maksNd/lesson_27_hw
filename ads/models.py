from django.core.validators import MinLengthValidator
from django.db import models

from ads.validators import check_not_published
from users.models import User


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=10, unique=True, validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    name = models.CharField(max_length=150, validators=[MinLengthValidator(10)], blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    is_published = models.BooleanField(default=False, validators=[check_not_published])
    image = models.ImageField(null=True, blank=True, upload_to='ad_images')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Selection(models.Model):
    name = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)
