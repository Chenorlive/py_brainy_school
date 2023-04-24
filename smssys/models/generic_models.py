from django.db import models
from django.utils import timezone


class GenderTypes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name


class NationalityType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    

    def __str__ (self):
        return self.name


class MaritalStatusType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
  

    def __str__(self):
        return self.name






