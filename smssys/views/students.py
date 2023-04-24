from django.shortcuts import render
from django.db.models import Prefetch
from django.views.decorators.csrf import csrf_exempt
from ..functions import login_required
from ..models import (
    Student, StudentClass, Schedule, StudentGrade, SchedulePeriod, TeacherSubjectClass, 
    Subject, AcademicSemesterPeriod
)
from django.db.models import Q



@login_required
def studentIndex(request):

    user = request.user
    studentClass = StudentClass.objects.get(student__user__username=user.username)
    period = SchedulePeriod.objects.all()
    schedules = Schedule.objects.all().filter(
        scheduleClass__pk=studentClass.studentClass.pk
    ).select_related('period')

    context = {'schedules': schedules, 'period': period, 'stClass': studentClass, 'title':'Dashboard'}
    return render(request, 'students/index.html', context)


# def studentGrade(request):
#     user = request.user
#     s_semester = request.session['school_semeter']

#     return render(request, 'students/grade.html')

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

    

    context = {"grades": sGrade, "subjects": subject, 'title':'Grades'} 

    return render(request, 'students/studentGrade.html', context)







