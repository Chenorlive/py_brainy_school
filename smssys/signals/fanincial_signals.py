from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from ..models import (
    AcademicSchoolYear
)


@receiver(pre_save, sender=AcademicSchoolYear)
def  deactive_pre_school(sender, instance, *args, **kwargs):
    AcademicSchoolYear.objects.all().update()

