from django.contrib.auth.models import AbstractUser, UserManager
from .generic_models import models, GenderTypes, NationalityType


class MyUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    password_hint = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField("user_image",null=True, blank=True)
    gender = models.ForeignKey(GenderTypes,on_delete=models.CASCADE, null=True, blank=True)
    nationality = models.ForeignKey(NationalityType, on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['first_name', 'last_name']





