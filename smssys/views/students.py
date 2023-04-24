from django.shortcuts import render
from django.db.models import Prefetch
from django.views.decorators.csrf import csrf_exempt
from ..functions import login_required
from ..models import (
    Student, StudentClass, Schedule, StudentGrade, SchedulePeriod, TeacherSubjectClass, 
    Subject, AcademicSemesterPeriod
)
from django.db.models import Q
from django.contrib import messages



@login_required
def studentIndex(request):

    user = request.user
    studentClass = StudentClass.objects.get(student__user__username=user.username)
    period = SchedulePeriod.objects.all()
    schedules = Schedule.objects.all().filter(
        scheduleClass__pk=studentClass.studentClass.pk
    ).select_related('period')

    context = {'schedules': schedules, 'period': period, 'stClass': studentClass}
    return render(request, 'students/index.html', context)



def studentGrade(request, ayid):

    user = request.user
    s_semester = request.session['school_semeter']

    print(s_semester)

    st_class = StudentClass.objects.get(
        Q(student__user__username=user.username) &
        Q(academicSemester__pk=int(s_semester))
    )

    subject = TeacherSubjectClass.objects.all().filter(
        teacherClass__pk=st_class.pk
    )

    sGrade = StudentGrade.objects.all().filter(
        Q(studentClass__student__user__username=user.username) &
        Q(academicSemesterPeriod__academicSemester__academicSchoolYear__pk=int(ayid)) 
    ).select_related('studentClass__studentClass').select_related('academicSemesterPeriod')

    

    context = {"grades": sGrade, "subjects": subject} 

    return render(request, 'students/studentGrade.html', context)



@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        new_password1 = request.POST['new_password1']
        user = request.user
        if old_password == 'none' or new_password == 'none' or new_password1 == 'none':
            messages.error(request, 'Please fill in all fields')
            return redirect('change_password')
        if not user.check_password(old_password):
            messages.error(request, "old password wrong")
            return redirect('change_password')
        if not new_password == new_password1:
            messages.error(request, "new password don't matches")
            return redirect('change_password')
        user.set_password(new_password)
        user.password_hint = new_password
        user.save()
        messages.success(request, 'Password successful changed')
        return redirect('user_profile')
    return render(request, 'users/change_password.html', {'year': datetime.now().year, 'title': 'change Password'})






