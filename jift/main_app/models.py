from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, default='Name')
    description = models.CharField(max_length=1000, default='Description')
    link = models.CharField(max_length=200, default='Link')

