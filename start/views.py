from django.shortcuts import render


def start(request):
    return render(request, 'HR_CRM_System/start.html')

