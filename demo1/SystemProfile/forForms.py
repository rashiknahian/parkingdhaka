from django import forms
from .models import *

class SignupFrom(forms.ModelForm):
    userName = forms.CharField(max_length=100, label='Username')
    userPass = forms.CharField(max_length=100,
                               widget=forms.PasswordInput, label='Password')
    userPass2 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput, label='Confirm Password')
    firstName = forms.CharField(max_length=100, label='First Name')
    lastName = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(max_length=100, label='Email')

    class Meta:
        model = SystemProfile
        fields = ("userName", "userPass", "userPass2", "firstName", "lastName", "email",
                  "NID", "Registration","vehicleType", "vehicleCC", 'presentAddress',
                  'permanentAddress','phone','occupation','picture','drivingLicense')


class LoginForm(forms.Form):
    userName = forms.CharField(max_length=100, label='Username')
    userPass = forms.CharField(max_length=100,
                               widget=forms.PasswordInput, label='Password')