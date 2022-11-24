from django.shortcuts import render


def start(request):
    return render(request, 'HR_CRM_System/start.html')

def login(request):
    return render(request, 'HR_CRM_System/login.html')

def registration_user(request):
    return render(request, 'HR_CRM_System/registration.html')