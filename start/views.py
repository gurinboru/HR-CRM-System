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
    return render(request, 'start/start.html',content)

def getCerJobSeek(request,pk):
    jobSeek = JobSeek.objects.get(id = pk)
    content = {
        "jobSeek" : jobSeek
    }

def getCerCandidate(request,pk):
    candidate = Candidate.objects.get(id = pk)
    content = {
        "jobSeek" : candidate
    }

def getCerJob(request,pk):
    job = Job.objects.get(id = pk)
    content = {
        "job" : job
    }

def getJob(request):
    jobs = Job.objects.all()
    content = {
        "jobs" : jobs
    }
    return render(request, 'start/start.html',content)

def addCurJobSeek(request):
    if request.method == 'POST':
        pass

def addJob(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('/jobs')
    form = AddJobForm()
    content = {
        'form':form
    }
    return render(request,'',content)

def addCandidate(request):
    if request.method == 'POST':
        pass

def add_candidate(request):
    return render(request, 'start/add_candidate.html')