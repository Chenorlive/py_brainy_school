from .generic_models import models
from .users_models import MyUser


# model
class StaffTypes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Staff(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    staffType = models.OneToOneField(StaffTypes, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

    def __str__ (self):
        return f"{self.user.first_name} {self.user.last_name}"