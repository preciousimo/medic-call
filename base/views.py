from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
# from .models import User
# from .forms import MyUserCreationForm
# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('backend')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

    # context = {'page': page}
    return render(request, 'base/registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('frontend')


def frontend(request):
    return render(request, "base/frontend.html")

@login_required(login_url='login')
def backend(request):
    return render(request, "base/backend.html")