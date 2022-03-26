from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from base.models import Patient 
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('backend')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'base/registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('frontend')


def frontend(request):
    return render(request, "base/frontend.html")

@login_required(login_url='login')
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q) | Q(age__icontains=q) | Q(gender__icontains=q) | Q(note__icontains=q)
        ).order_by('-created_at')
    else:
        all_patient_list = Patient.objects.all().order_by('-created_at')
    paginator = Paginator(all_patient_list, 5)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)

    return render(request, "base/backend.html", {"patients":all_patient})

@login_required(login_url='login')
def add_patient(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender' ) or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Patient added successfully!")
            return HttpResponseRedirect('/backend')
    else:
        return render(request, "base/add.html")

@login_required(login_url='login')
def patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    if patient != None:
        return render(request, "base/edit.html", {'patient':patient})