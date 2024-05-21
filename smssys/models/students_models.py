# import of extenal classes or library
from .generic_models import models
from django.conf import settings
from .school_models import Class, AcademicSemester
from django.utils import timezone
import uuid


# model

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    stid = models.CharField(max_length=20, unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_creator")


    def __str__ (self):
        return f"{self.user.first_name} {self.user.last_name}"


class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    studentClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    academicSemester = models.ForeignKey(AcademicSemester, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )


    def __str__(self):
        return f'{self.student.user.first_name} ({self.studentClass.name})'
    


class StudentClassReport(models.Model):
    RStatue = (
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
        ('Ongoing', 'Ongoing')
    )
    studentClass = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    average = models.FloatField()
    statue = models.CharField(max_length=20)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )



class StudentBillingReport(models.Model):
    amount = models.FloatField()
    balance = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )



# Perent models

class Parent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_Alive = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="P_creator")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class FamilyMember(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )


    def __str__(self):
        return f"{self.student.user.first_name} ({self.parent.user.first_name})"



