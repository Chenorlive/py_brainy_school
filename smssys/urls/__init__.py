from django.urls import path


from ..views import (
    studentIndex, logout_view, login_view, teacherIndex, teacherAddGrade, classList, teacherClass,
    studentGrade, createStudent, change_password, studentDetails,
    
)


urlpatterns = [
    # adminstrator

    path('student/add', createStudent, name="add_student"),

    # authentication
    path('', login_view, name="login"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),


    # Student
    path('student/', studentIndex, name="student_index"),
    path('student/grade/<str:ayid>', studentGrade, name="student_grade"),
    path('student/details/', studentDetails, name="student_details" ),

    # teacher
    path('teachers/', teacherIndex, name="teacher_index"),
    path('teachers/class/<int:tscid>/', teacherClass, name="teacher_class"),
    path('teachers/class/<int:cid>/list/', classList, name="teacher_class_list"),

    path('grades/add/<tscid>/<pid>/', teacherAddGrade, name="teacher_add_grade"),
    
    #user
    path('user/password/change/', change_password, name="change_password")
    

]