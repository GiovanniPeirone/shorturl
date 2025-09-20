from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

# Create your views here.
