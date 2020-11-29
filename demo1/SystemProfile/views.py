from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


from .models import *
from .forForms import *
# Create your views here.

@login_required(login_url='userLogin')
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupFrom(request.POST or None, request.FILES)
        if form.is_valid():
            if form.cleaned_data['userPass'] == form.cleaned_data['userPass2']:
                userReg = form.save(commit=False)
                u = User.objects.create_user(username = form.cleaned_data['userName'],
                                             first_name = form.cleaned_data['firstName'],
                                             last_name = form.cleaned_data['lastName'],
                                             email = form.cleaned_data['email'])
                u.set_password(form.cleaned_data['userPass'])
                u.save()

                userReg.systemUser = u
                userReg.save()
                return redirect(reverse("userLogin"))

        context = {
            'form':form,
            'pageTitle':'User Registration',
            'submitType':'Sign Up',
            'signup_form':True
        }
        return render(request, 'home.html', context=context)


    if request.method == "GET":
        form = SignupFrom()
        context = {
            'form':form,
            'pageTitle':'User Registration',
            'submitType':'Sign Up',
            'togglePage':'Login Now',
            'location': 'userLogin',
            'signup_form':True
        }
        return render(request, 'home.html', context=context)


def userLogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            userName = form.cleaned_data["userName"]
            userPass = form.cleaned_data["userPass"]
            try:
                user_auth = authenticate(request,username=userName, password=userPass)
                login(request, user_auth)
                return redirect(reverse("home"))
            except:
                msg = "Wrong Credetials or User does not exists"
            context = {
                'msg': msg,
                'form': form,
                'login_form':True
            }
            return render(request, 'home.html', context=context)

    if request.method == "GET":
        form = LoginForm()
        context = {
            'form':form,
            'pageTitle':'User Login',
            'submitType':'Login',
            'togglePage':'Sign Up Now',
            'location':'signup',
            'login_form':True
        }
        return render(request, 'home.html', context=context)

@login_required(login_url='userLogin')
def userLogout(request):
    logout(request)
    return redirect(reverse("home"))