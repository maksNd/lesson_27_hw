from django.db import models
from _data_source.csv_to_json import load_data_to_model


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Ad(models.Model):
    # category = models.ForeignKey(Categories, on_delete = models.SET_NULL)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)
