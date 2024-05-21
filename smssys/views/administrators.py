from django.shortcuts import render, redirect
from ..functions import login_required, gen_stid
from ..forms import StudentForm
from ..models import MyUser, Student, GenderTypes, NationalityType

from django.views import View 



@login_required
def adminIndex(request):

    user = request.user

    context = {}
    return render(request, 'students/index.html', context)


def createStudent(request):

    if request.method == 'POST':
        post = request.POST

        user = request.user

        f_name = post['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        dob = request.POST['dob']
        address = request.POST['address']
        image = request.FILES.get('image')
        gender = request.POST['gender']
        nationality = request.POST['nationality']

        gendertypes = GenderTypes.objects.get(pk=gender)
        nationalitytype = NationalityType.objects.get(pk=nationality)

        password = MyUser.objects.make_random_password(length=6)
        username = gen_stid()

        if image:
            s_user = MyUser.objects.create(
                first_name=f_name, last_name=l_name, username=username,
                email=email, password_hint=password, address=address,
                phone_number=phone_number, date_of_birth=dob, gender=gendertypes,
                image=image, nationality=nationalitytype,
            )
        else:
            s_user = MyUser.objects.create(
                first_name=f_name, last_name=l_name, username=username,
                email=email, password_hint=password, address=address,
                phone_number=phone_number, date_of_birth=dob, gender=gendertypes,
                image=image, nationality=nationalitytype,
            )

        s_user.set_password(password)

        s_user.save()

        st = Student.objects.create(
            user=s_user, created_by=user, stid=username
        )

        s_semester = request.session['school_semeter']

    
    form = StudentForm
    genders = GenderTypes.objects.all()
    nationality = NationalityType.objects.all()
    context = {'form': form, 'genders': genders, 'nationalities': nationality}
    return render(request, 'adminstrators/createStudent.html', context)



class CreateTeacher(View):

    def get(request):
        return()


