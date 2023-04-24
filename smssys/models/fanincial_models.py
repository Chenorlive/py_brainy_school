from .generic_models import models
from django.conf import settings
from .school_models import Class, AcademicSchoolYear, Subject
from .students_models import StudentClass
from django.utils import timezone



class BillingItemType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)



class ClassBillingItems(models.Model):
    billingClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    billingYear = models.ForeignKey(AcademicSchoolYear, on_delete=models.CASCADE)
    billingtype = models.ForeignKey(BillingItemType, on_delete=models.CASCADE)
    amountInUSD = models.FloatField()
    amountInLRD = models.FloatField()
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.billingtype} ({self.billingClass})'
    
    class Meta:
        unique_together = ('billingClass', 'billingYear', 'billingtype')


class ClassBillingSummary(models.Model):
    amountInUSD = models.FloatField()
    amountInLRD = models.FloatField()
    billingClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    billingYear = models.ForeignKey(AcademicSchoolYear, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    
    class Meta:
        unique_together = ('billingClass', 'billingYear')


class Payment(models.Model):
    currencyType = (
        ('USD', 'USD'),
        ('LRD', 'LRD')
    )
    currency = models.CharField(max_length=100, choices=currencyType)
    amount = models.FloatField()
    studentClass = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    recorded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)





