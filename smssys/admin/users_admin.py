
from django import forms
from ..models.users_models import MyUser
from django.contrib.auth.admin import (UserAdmin as BaseAdmin)
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .adminStackedInline import StudentAdminStackedInline, StaffAdminStackedInline, TeacherAdminStackedInline

# Register your models here.


class UserCreationFrom(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmation Password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeform(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseAdmin):
    forms = UserChangeform
    add_form = UserCreationFrom
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'is_admin')
    list_filter = ('is_staff', 'is_admin')
    fieldsets = (
        ('Personal Info', {'fields': ('username','email', 'first_name', 'last_name', 'password', 'password_hint', 
                                      'date_of_birth', 'phone_number', 'address', 'image', 'gender', 'nationality', )}),
        ('Permission', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin',  'groups', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2', 'password_hint', 'first_name', 'last_name', 'date_of_birth',
                            'phone_number', 'address', 'image', 'gender', 'nationality',),
                }),
        ('Permission', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'groups', 'user_permissions')})
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ()
    #inlines = [StudentAdminStackedInline, TeacherAdminStackedInline, StaffAdminStackedInline]



