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

    context = {'schedules': schedules, 'period': period, 'stClass': studentClass}
    return render(request, 'students/index.html', context)



def studentGrade(request):

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
        Q(academicSemesterPeriod__academicSemester__pk=int(s_semester)) 
    )

    

    context = {"grades": sGrade, "subjects": subject} 

    return render(request, 'students/studentGrade.html', context)







