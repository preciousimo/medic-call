from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from base.models import Patient 
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def frontend(request):
    return render(request, "base/frontend.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
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

#Function to access patient individually
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    if patient != None:
        return render(request, "base/edit.html", {'patient':patient})

#Function to edit patient
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def edit_patient(request):
    if request.method == "POST":
        patient = Patient.objects.get(id = request.POST.get('id'))
        if patient != None:

            patient.name = request.POST.get('phone')
            patient.name = request.POST.get('email')
            patient.name = request.POST.get('age')
            patient.name = request.POST.get('gender')
            patient.name = request.POST.get('note')
            patient.save()

            messages.success(request, "Patient updated successfully !")
            return HttpResponseRedirect('/backend')

#Function to delete patient
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    patient.delete()

    messages.success(request, "Patient removed successfully !")
    return HttpResponseRedirect('/backend')