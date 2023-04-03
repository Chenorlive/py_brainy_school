from ..models import ( 
    MyUser, GenderTypes, MaritalStatusType, NationalityType, StudentGrade,
    School, AcademicSchoolYear, AcademicSemester, AcademicSemesterPeriod, 
    AcademicSemesterType, PeriodType, Schedule, SchedulePeriod, Subject, Class, ClassType,
    Staff, StaffTypes, Student, StudentClass, Parent, FamilyMember, Teacher, TeacherSubjectClass,

 )

from django.contrib import admin


#user
class UserAdminStackedInline(admin.StackedInline):
    model = MyUser
    extra = 1


#generic
class GenderTypesAdminStackedInline(admin.StackedInline):
    model = GenderTypes
    extra = 1


class MaritalStatusAdminStackedInline(admin.StackedInline):
    model = MaritalStatusType
    extra = 1


class NationalitysAdminStackedInline(admin.StackedInline):
    model = NationalityType
    extra = 1


# school
class AcademicSchoolYearAdminStackedInline(admin.StackedInline):
    model = AcademicSchoolYear
    extra = 1


class SchoolAdminStackedInline(admin.StackedInline):
    model = School
    extra = 1


class AcademicSemesterAdminStackedInline(admin.StackedInline):
    model = AcademicSemester
    extra = 1


class AcademicSemesterTypeAdminStackedInline(admin.StackedInline):
    model = AcademicSemesterType
    extra = 1


class AcademicSemesterPeriodAdminStackedInline(admin.StackedInline):
    model = AcademicSemesterPeriod
    extra = 1



class PeriodTypeAdminStackedInline(admin.StackedInline):
    model = PeriodType
    extra = 1


class ScheduleAdminStackedInline(admin.StackedInline):
    model = Schedule
    extra = 1


class SchedulePeriodAdminStackedInline(admin.StackedInline):
    model = SchedulePeriod
    extra = 1


class SubjectAdminStackedInline(admin.StackedInline):
    model = Subject
    extra = 1

class ClassAdminStackedInline(admin.StackedInline):
    model = Class
    extra = 1


class ClassTypeAdminStackedInline(admin.StackedInline):
    model = ClassType
    extra = 1


#staff
class StaffTypeAdminStackedInline(admin.StackedInline):
    model = StaffTypes
    extra = 1


class StaffAdminStackedInline(admin.StackedInline):
    model = Staff
    extra = 1


# student
class StudentAdminStackedInline(admin.StackedInline):
    model = Student
    extra = 1


class StudentClassAdminStackedInline(admin.StackedInline):
    model = StudentClass
    extra = 1


class ParentAdminStackedInline(admin.StackedInline):
    model = Parent
    extra = 1


class FamilyMemberAdminStackedInline(admin.StackedInline):
    model = FamilyMember
    extra = 1


#Teacher
class TeacherAdminStackedInline(admin.StackedInline):
    model = Teacher
    extra = 1


class TeacherSubjectClassAdminStackedInline(admin.StackedInline):
    model = TeacherSubjectClass
    extra = 1


# StudentGrade
class StudentGradeAdminStackedInline(admin.StackedInline):
    model = StudentGrade
    extra = 1