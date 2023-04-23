from django.urls import path
from ..views import (
    studentIndex, logout_view, login_view, teacherIndex, teacherAddGrade, classList, teacherClass,
    studentGrade, createStudent
    
)


urlpatterns = [
    # adminstrator

    path('student/add', createStudent, name="add_student"),

    # authentication
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),


    # Student
    path('student/', studentIndex, name="student_index"),
    path('student/grade', studentGrade, name="student_grade"),

    # teacher
    path('teachers/', teacherIndex, name="teacher_index"),
    path('teachers/class/<int:tscid>/', teacherClass, name="teacher_class"),
    path('teachers/class/<int:cid>/list/', classList, name="teacher_class_list"),

    path('grades/add/<tscid>/<pid>/', teacherAddGrade, name="teacher_add_grade"),
    

]