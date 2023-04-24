from django.shortcuts import render, redirect
from ..functions import login_required
from ..forms import StudentForm
from ..models import MyUser, Student, GenderTypes, NationalityType

from django.views import View 



@login_required
def adminIndex(request):

    user = request.user

    context = {}
    return render(request, 'students/index.html', context)


def createStudent(request):

    gender = GenderTypes.objects.all()
    nationality = NationalityType.objects.all()

    if request.method == 'POST':
        post = request.POST

        user = MyUser(
            first_name=post['f_name'], last_name=post['l_name'], email=post['email'],
            gender=post['gender'],
        )

        student = Student(

        )

        f_name = post['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        dob = request.POST['dob']
        address = request.POST['address']
        image = request.FILES.get('image')
        gender = request.POST['gender']
        nationality = request.POST['nationality']

        
        #username = f'SID{}'




        period_pk = request.POST['period']
        stClass = request.POST['student']
        tscid = request.POST['teacher']
        if_update = request.POST['if_update']
        s_semester = request.session['school_semeter']

    
    form = StudentForm
    gender = GenderTypes.objects.all()
    nationality = NationalityType.objects.all()
    context = {'form': form, 'gender': gender, 'nationality': nationality}
    return render(request, 'adminstrators/createStudent.html', context)



class CreateTeacher(View):

    def get(request):
        return()


