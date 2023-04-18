from django.shortcuts import render, redirect



@login_required
def adminIndex(request):

    user = request.user
    studentClass = StudentClass.objects.get(student__user__username=user.username)
    period = SchedulePeriod.objects.all()
    schedules = Schedule.objects.all().filter(
        scheduleClass__pk=studentClass.studentClass.pk
    ).select_related('period')

    context = {'schedules': schedules, 'period': period, 'stClass': studentClass}
    return render(request, 'students/index.html', context)
