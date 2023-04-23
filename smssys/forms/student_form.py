from django import forms
from ..models import Student, MyUser


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'is_admin')


class StudentForm(forms.ModelForm):
    user = MyUserForm

    class Meta:
        model = Student
        fields = ('user', 'isActive')

