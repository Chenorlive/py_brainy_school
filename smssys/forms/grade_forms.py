from django import forms
from ..models import StudentGrade

class GradeForm(forms.ModelForm):

    class Meta:
        model = StudentGrade
        fields = '__all__'

