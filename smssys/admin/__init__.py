from django.contrib import admin
from .users_admin import UserAdmin

from ..models import ( 
    MyUser, GenderTypes, MaritalStatusType, NationalityType, StudentGrade,
    School, AcademicSchoolYear, AcademicSemester, AcademicSemesterPeriod, 
    AcademicSemesterType, PeriodType, Schedule, SchedulePeriod, Subject, 
    Class, ClassType, Staff, StaffTypes, Student, StudentClass, Parent, 
    FamilyMember, Teacher, TeacherSubjectClass, StudentAttendent
 )

from .adminModelsStack import (
    StudentAdmin
)

from django.contrib import admin


# Register models for super admin

admin.site.register(MyUser, UserAdmin)


# school
admin.site.register(AcademicSchoolYear)

admin.site.register(AcademicSemester)

admin.site.register(AcademicSemesterPeriod)

admin.site.register(Schedule)

admin.site.register(AcademicSemesterType)

admin.site.register(PeriodType)

admin.site.register(SchedulePeriod)

admin.site.register(Subject)

admin.site.register(Class)

admin.site.register(ClassType)

admin.site.register(School)


#staff
admin.site.register(Staff)

admin.site.register(StaffTypes)

# generic
admin.site.register(GenderTypes)

admin.site.register(MaritalStatusType)

admin.site.register(NationalityType)

# grade
admin.site.register(StudentGrade)


# Student
admin.site.register(StudentClass)

admin.site.register(Student)

admin.site.register(Parent)

admin.site.register(FamilyMember)

# teachers
admin.site.register(Teacher)

admin.site.register(TeacherSubjectClass)

# Attendent

admin.site.register(StudentAttendent)

# fanincial




