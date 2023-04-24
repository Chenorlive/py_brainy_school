from .generic_models import models
from .school_models import AcademicSemesterPeriod
from .students_models import StudentClass
from .teachers_models import TeacherSubjectClass
from django.utils import timezone
from django.conf import settings


class StudentGrade(models.Model):
    studentClass = models.ForeignKey(StudentClass, on_delete=models.CASCADE, related_name='s_class')
    academicSemesterPeriod = models.ForeignKey(AcademicSemesterPeriod, on_delete=models.CASCADE)
    teacherClass = models.ForeignKey(TeacherSubjectClass, on_delete=models.CASCADE)
    grade = models.FloatField()
    grade_letter = models.CharField(max_length=5, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )


    def __str__(self):
        return f"{self.grade} {self.grade_letter}"
    
    def save(self, *args, **kwargs):
        g = self.grade
        if int(g) >= 90:
            self.grade_letter = 'A'
        if int(g) >= 80:
            self.grade_letter = 'B'
        if int(g) >= 70:
            self.grade_letter = 'C'
        if int(g) <= 70:
            self.grade_letter = 'F'
        super().save(*args, **kwargs)


        




    
