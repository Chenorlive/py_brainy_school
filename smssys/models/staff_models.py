from .generic_models import models
from django.conf import settings
from django.utils import timezone


# model
class StaffTypes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )



class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staffType = models.OneToOneField(StaffTypes, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Staff_creator")


    def __str__ (self):
        return f"{self.user.first_name} {self.user.last_name}"