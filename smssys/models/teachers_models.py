from .generic_models import models
from django.conf import settings
from .school_models import Class, AcademicSchoolYear, Subject
from django.utils import timezone


# model
class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    isActive = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Teacher_creator" )


    def __str__ (self):
        return f"{self.user.first_name} {self.user.last_name}"


class TeacherSubjectClass(models.Model):

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    teacherClass = models.ForeignKey(Class, on_delete=models.CASCADE)
    academicSchoolYear = models.ForeignKey(AcademicSchoolYear, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)


    def __str__(self):
        return f'{self.teacher.user.first_name} ({self.teacherClass.name}) ({self.subject.name})'
    
    class Meta:
        unique_together = ('teacherClass', 'academicSchoolYear', 'subject')




    