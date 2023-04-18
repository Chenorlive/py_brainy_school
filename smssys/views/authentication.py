from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from ..models import Student, Teacher, Staff, AcademicSchoolYear, AcademicSemester
from django.db.models import Q 


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        print(user)
        if user is None:
            messages.error(request, 'username or password wrong')
            return redirect('login')
         #login the 
        date = datetime.now()

        

        s_year = AcademicSchoolYear.objects.all().filter(
            Q(isActive=True)
        ).first()

        s_semester = AcademicSemester.objects.all().filter(
            Q(isActive=True) & 
            Q(academicSchoolYear__pk=s_year.pk)
        ).first()
        login(request, user)
        msg = f'{username} have successful login'
        request.session['school_year'] = s_year.pk
        request.session['school_semeter'] = s_semester.pk
        
        s_user = Student.objects.select_related('user').all().filter(user__username=username).first() # if its student
        print(s_user)
        if s_user and s_user.isActive:
            messages.success(request, msg)
            return redirect('student_index') # sent user to student dashboard
        
        t_user = Teacher.objects.select_related('user').all().filter(user__username=username).first() # if its teacher
        print(t_user)
        if t_user and t_user.isActive:
            print('t')
            messages.success(request, msg)
            return redirect('teacher_index') # sent user to teacher dashboard
        
        st_user = Staff.objects.select_related('user').all().filter(user__username=username).first() # if its teacher
        print(st_user)
        if st_user and st_user.isActive:
            print('st')
            messages.success(request, msg)
            return redirect('staff_index') # sent user to teacher dashboard
        
        #if user.is_admin: # login admin
        #    messages.success(request, 'you have successful login')
        #    return redirect('admin_index') # sent user to admin dashboard
        
        
    return render(request, 'authentication/login.html', {'year': datetime.now().year, 'title': 'Login'})


def logout_view(request):
    logout(request)
    return redirect('login')



