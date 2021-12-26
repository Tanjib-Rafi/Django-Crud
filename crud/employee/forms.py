from django import forms
from django.db import models
from .models import Employee
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model


UserModel = get_user_model()

GENDER_CHOICES = [
   ('Male', 'Male'),
   ('Female', 'Female')
    ]

role_choice = [
    ('admin', 'admin'),
    ('employee', 'employee') 
    ]

class CreateEmployee(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    #role = models.CharField(max_length=50,choices=role_choice,default="employee")
    # password1 : forms.CharField(label='password', widget=forms.PasswordInput)
    # password2 : forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['name','email','password','gender','date_of_birth','role']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : 'Enter Your Name', 'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'Enter Your Email', 'class': 'form-control'}),
            'password' : forms.PasswordInput(render_value=True,attrs={'placeholder' : 'Enter Your Password', 'class': 'form-control'}),
            #'password2' : forms.PasswordInput(render_value=True,attrs={'placeholder' : 'Enter Your Password', 'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'role' : forms.Select(attrs={'class': 'btn btn-warning'}),
        }