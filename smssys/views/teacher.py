from django.shortcuts import render, redirect
from django.forms import formset_factory, inlineformset_factory
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from ..functions import login_required
from ..models import (
    Teacher, TeacherSubjectClass, Schedule, StudentClass, StudentGrade,
    AcademicSemesterPeriod, SchedulePeriod, PeriodType
)
from ..forms import GradeForm
from django.db.models import Q 


@login_required
def teacherIndex(request):
    user = request.user

    tSubjectClass = TeacherSubjectClass.objects.all().filter(
        teacher__user__username=user.username
    ).select_related('teacher__user')

    context = {'tsubjectClass': tSubjectClass}
    return render(request, 'teachers/index.html', context)



def teacherClass(request, tscid):

    period = SchedulePeriod.objects.all()
    tSubjectClass = TeacherSubjectClass.objects.get(pk=tscid)

    schedule = Schedule.objects.all().filter(
        Q(scheduleClass__pk=tSubjectClass.teacherClass.pk) &
        Q(subject__pk=tSubjectClass.subject.pk)
    ).order_by('day').select_related('period')
    

    context = {'schedules': schedule, 'period': period, 'tSubjectClass': tSubjectClass }
    return render(request, 'teachers/teacherclass.html', context)



def classList(request, cid):

    clist = StudentClass.objects.all().filter(
        studentClass__pk=cid
    )
    context = {'clist': clist,}
    return render(request, 'teachers/classlist.html', context)



def teacherStudentGrade(request, cid):

    user = request.user
    teacher = Teacher.objects.get(user__username=user.username)

    clist = StudentClass.objects.all().filter(
        studentClass__pk=cid
    )
    context = {'clist': clist, 'teacher': teacher}
    return render(request, 'teachers/classlist.html', context)


def teacherAddGrade(request, tscid, pid):

    if request.method == 'POST':
        grade = request.POST['grade']
        #period_pk = request.POST['period']
        stClass = request.POST['student']
        tscid = request.POST['teacher']
        if_update = request.POST['if_update']
        s_semester = request.session['school_semeter']
      
        period = AcademicSemesterPeriod.objects.all().filter(
            academicSemester__pk=pid
        )
        tclass = TeacherSubjectClass.objects.all().filter(
            pk=tscid
        )

        if if_update == "1":
            sGrade = StudentGrade.objects.all().filter(
                Q(studentClass__pk=stClass) & 
                Q(academicSemesterPeriod__pk=pid) &
                Q(teacherClass__pk=tscid)
            ).first()
            sGrade.grade = grade
        else:
            sGrade = StudentGrade(
                studentClass__pk=stClass,
                academicSemesterPeriod=period,
                teacherClass__pk=tscid,
                grade=grade,
            )
        sGrade.save()
        return redirect(f'/grades/add/{tscid}/{pid}')

    tSubjectClass = TeacherSubjectClass.objects.all().filter(pk=tscid).select_related('teacher').first()
    clist = StudentClass.objects.all().filter(
        studentClass__pk=tSubjectClass.teacherClass.pk
    ).select_related('student')

    period = AcademicSemesterPeriod.objects.all()

    context = {'clist': clist, 'teacher': tSubjectClass, 'pid': pid}
    return render(request, 'teachers/addGrade.html', context)



def addgrade(request, tscid):

    if request.method == 'POST':
        grade = request.POST['grade']
        period_pk = request.POST['period']
        stClass = request.POST['student']
        tscid = request.POST['teacher']
        s_semester = request.session['school_semeter']

        period = AcademicSemesterPeriod.objects.all().filter(
            academicSemester__pk=period_pk
        )
        tclass = TeacherSubjectClass.objects.all().filter(
            pk=tscid
        )

        sGrade = StudentGrade(
            studentClass__pk=stClass,
            academicSemesterPeriod=period,
            teacherClass__pk=tscid,
            grade=grade,
         )
        sGrade.save()
        

    context = {}

    return render(request, 'teachers/addGrade.html', context)
