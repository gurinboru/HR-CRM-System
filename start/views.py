from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def start(request):
    return render(request, 'start/start.html')

def getCandidates(request):
    candidates = Candidate.objects.all()
    content = {
        "candidates" : candidates
    }
    return render(request, 'start/candidates.html',content)

def getJobSeek(request):
    jobSeek = JobSeek.objects.all()
    content = {
        "jobSeek" : jobSeek
    }
    return render(request, 'start/jobseek.html',content)

def getCerJobSeek(request,pk):
    jobSeek = JobSeek.objects.get(id = pk)
    content = {
        "jobSeek" : jobSeek
    }
    return render(request, 'start/cerjobseek.html', content)
def getCerCandidate(request,pk):
    candidate = Candidate.objects.get(id = pk)
    jobseek = JobSeek.objects.filter(candidate = candidate)
    content = {
        "candidate" : candidate,
        "jobseek":jobseek
    }
    return render(request, 'start/cercandidate.html', content)

def getCerJob(request,pk):
    job = Job.objects.get(id = pk)
    content = {
        "job" : job
    }
    return render(request, 'start/cerjob.html', content)

def getJob(request):
    jobs = Job.objects.all()
    content = {
        "jobs" : jobs
    }
    return render(request, 'start/jobs.html',content)

def addJob(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Job(name = cd['name'], salary = cd['salary'], expirence = cd['expirence'], employment = cd['employment'], definition = cd['definition'],
                      id_status = StatusJob.object.get(status = cd['status']), user = request.user).save()
            return redirect('/jobs')
        else:
            messages.error(request, 'Аккаунт уже существует или введены неверные данные')
    form = AddJobForm()
    content = {
        'form':form
    }
    return render(request,'',content)

def addCandidate(request):
    if request.method == 'POST':
        form = AddCandidateForm(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Candidate(name = cd['name'], phone = cd['phone'], email = cd['email'], sex = cd['sex'], photo = cd['photo'],
                      birthdate = cd['birthdate'], cv = cd['cv']).save()
            return redirect('/candidates')
        else:
            messages.error(request, 'Аккаунт уже существует или введены неверные данные')
    form = AddCandidateForm()
    content = {
        "form":form
    }
    return render(request, 'start/add_candidate.html', content)