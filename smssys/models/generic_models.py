from django.db import models


class GenderTypes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class NationalityType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__ (self):
        return self.name


class MaritalStatusType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name






