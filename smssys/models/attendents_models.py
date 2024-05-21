from .generic_models import models
from .school_models import AcademicSemesterPeriod
from .students_models import StudentClass
from .teachers_models import TeacherSubjectClass
from django.utils import timezone
from django.conf import settings


class StudentAttendent(models.Model):
    studentClass = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    academicSemesterPeriod = models.ForeignKey(AcademicSemesterPeriod, on_delete=models.CASCADE)
    teacherClass = models.ForeignKey(TeacherSubjectClass, on_delete=models.CASCADE)
    attendent = models.BooleanField()
    date = models.DateTimeField()
    comment = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )


    def __str__(self):
        return f"{self.studentClass.student} {self.attendent}"
    
  