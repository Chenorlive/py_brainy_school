from django import template
from ..models import TeacherSubjectClass
from django.db.models import Q

register = template.Library()


def teacherForSchedule(value):
    t = TeacherSubjectClass.objects.filter(
        Q(subject__name=value.subject.name) & 
        Q(teacherClass__name=value.scheduleClass.name)
    ).first()
    a = str(t)
    b = a.split('(')
    return b[0]


register.filter('teacherForSchedule', teacherForSchedule)


