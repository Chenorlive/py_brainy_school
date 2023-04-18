from django.shortcuts import render
from ..models import (
    FamilyMember, Parent, StudentClass, Schedule, SchedulePeriod
)
from ..functions import login_required



def parentIndex(request):

    user = request.user

    parent = Parent.objects.filter(user__username=user.username).select_related(
        'user'
    )

    students = FamilyMember.objects.all().filter(
        parent__pk=parent.pk
    )
    

    context = {'students': students,}
    return render(request, 'parent/index.html', context)



@login_required
def studentClass(request, stid):

    studentClass = StudentClass.objects.get(student__pk=stid)
    period = SchedulePeriod.objects.all()
    schedules = Schedule.objects.all().filter(
        scheduleClass__pk=studentClass.studentClass.pk
    ).select_related('period')

    context = {'schedules': schedules, 'period': period, 'stClass': studentClass}
    return render(request, 'students/index.html', context)


def studentbill(request, stcid):


    context = {'schedules': request.user,}
    return render(request, 'students/index.html', context)

