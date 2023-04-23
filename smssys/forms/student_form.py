from django import forms
from ..models import Student, MyUser


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'


class StudentForm(forms.ModelForm):
    user = MyUserForm

    class Meta:
        model = Student
        fields = '__all__'

