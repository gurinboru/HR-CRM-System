from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'authentication/login.html')

def registration_user(request):
    return render(request, 'authentication/registration.html')