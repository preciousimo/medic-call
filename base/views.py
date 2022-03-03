from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def frontend(request):
    return render(request, "base/frontend.html")

def backend(request):
    return render(request, "base/backend.html")