from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def auth_index(request):
    return render(request, "authorization/login.html")

def auth_registration(request):
    return render(request, "authorization/registration.html")