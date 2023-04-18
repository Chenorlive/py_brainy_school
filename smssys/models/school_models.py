from .generic_models import models
from datetime import datetime
from django.db.models import UniqueConstraint, Q


class School(models.Model):
    name = models.CharField(max_length=200, )
    description = models.CharField(max_length=200)

    def __str__ (self):
        return self.name


class AcademicSchoolYear(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, null=True)
    date_recorded = models.DateField(default=datetime.now)
    isActive = models.BooleanField()
    year = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class AcademicSemesterType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AcademicSemester(models.Model):
    academicSchoolYear = models.ForeignKey(AcademicSchoolYear, on_delete=models.CASCADE)
    academicSemesterType = models.ForeignKey(AcademicSemesterType, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField()
    isActive = models.BooleanField()

    def __str__(self):
        return f'{self.academicSchoolYear.name} ({self.academicSemesterType.name})'


class PeriodType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_virtual = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AcademicSemesterPeriod(models.Model):
    periodType = models.ForeignKey(PeriodType, on_delete=models.CASCADE)
    academicSemester = models.ForeignKey(AcademicSemester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.periodType.name} {self.academicSemester.academicSemesterType.name}"


class ClassType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Class(models.Model):
    classType = models.ForeignKey(ClassType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SchedulePeriod(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    startTime = models.TimeField()
    endTime = models.TimeField()


class Schedule(models.Model):
    days = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    )
    period = models.ForeignKey(SchedulePeriod, on_delete=models.CASCADE)
    scheduleClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    academicYear = models.ForeignKey(AcademicSchoolYear, on_delete=models.CASCADE)
    day = models.CharField(max_length=100, choices=days)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('scheduleClass', 'academicYear', 'subject')

    def __str__(self):
        return f'{self.scheduleClass} ({self.subject}) ({self.period.name})'


