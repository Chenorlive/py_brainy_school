from django.shortcuts import render, redirect
from ..functions import login_required
from ..forms import StudentForm

from django.views import View 



@login_required
def adminIndex(request):

    user = request.user
    

    context = {}
    return render(request, 'students/index.html', context)


def createStudent(request):

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        period_pk = request.POST['period']
        stClass = request.POST['student']
        tscid = request.POST['teacher']
        if_update = request.POST['if_update']
        s_semester = request.session['school_semeter']

    form = StudentForm
    context = {'form': form}
    return render(request, 'adminstrators/createStudent.html', context)



class CreateTeacher(View):

    def get(request):
        return()


