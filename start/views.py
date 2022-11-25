import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def start(request):
    if (request.user.is_authenticated):
        return redirect('/candidates')
    return render(request, 'start/start.html')

@login_required(login_url='/login')
def getCandidates(request):
    candidates = Candidate.objects.all()
    content = {
        "candidates" : candidates
    }
    return render(request, 'start/candidates.html',content)

@login_required(login_url='/login')
def getJobSeek(request):
    jobSeek = JobSeek.objects.all()
    content = {
        "jobSeek" : jobSeek
    }
    return render(request, 'start/jobseek.html',content)

@login_required(login_url='/login')
def getCerJobSeek(request,pk):
    jobSeek = JobSeek.objects.get(id = pk)
    content = {
        "jobSeek" : jobSeek
    }
    return render(request, 'start/cerjobseek.html', content)

@login_required(login_url='/login')
def getCerCandidate(request,pk):
    candidate = Candidate.objects.get(id = pk)
    jobseek = JobSeek.objects.filter(candidate = candidate)
    content = {
        "candidate" : candidate,
        "jobseek":jobseek,
        }
    return render(request, 'start/cercandidate.html', content)

@login_required(login_url='/login')
def getCerJob(request,pk):
    job = Job.objects.get(id = pk)
    jobseek = JobSeek.objects.filter(job = job)
    content = {
        "job" : job,
        "jobseek": jobseek
    }
    return render(request, 'start/cerjob.html', content)

@login_required(login_url='/login')
def getJob(request):
    jobs = Job.objects.all()
    content = {
        "jobs" : jobs
    }
    return render(request, 'start/jobs.html',content)

@login_required(login_url='/login')
def addJob(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Job(name = cd['name'], salary = cd['salary'], expirence = cd['expirence'], employment = cd['employment'], definition = cd['definition'],
                      id_status = StatusJob.objects.get(status = cd['status']), user = request.user).save()
            return redirect('/jobs')
        else:
            messages.error(request, 'Вакансия уже существует или введены неверные данные')
    form = AddJobForm()
    content = {
        'form':form
    }
    return render(request,'start/add_job.html',content)

@login_required(login_url='/login')
def addCandidate(request):
    if request.method == 'POST':
        form = AddCandidateForm(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Candidate(name = cd['name'], phone = cd['phone'], email = cd['email'], sex = cd['sex'], position = cd['position'], photo = cd['photo'],
                      birthdate = cd['birthdate'], cv = cd['cv']).save()
            return redirect('/candidates')
        else:
            messages.error(request, 'Кандидат уже существует или введены неверные данные')
    form = AddCandidateForm()
    content = {
        "form":form
    }
    return render(request, 'start/add_candidate.html', content)

@login_required(login_url='/login')
def addJobSeek(request):
    if request.method == 'POST':
        form = AddJobSeek(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            JobSeek(job = Job.objects.get(cd['job']),
            candidate = Candidate.objects.get(cd['job']),
            offer = cd['offer'],
            offer_definition = cd['offer_definition'],
            release_date = cd['release_date'],
            denial_status = DenialStatus.objects.get(status = cd['denial_status']),
            call_status = CallStatus.objects.get(status = cd['call_status']),
            call_status_defenition = cd['call_status_defenition'],
            test_status = TestStatus.objects.get(status = cd['test_status']),
            test_status_defenition = cd['test_status_defenition'],
            meet_status = MeetStatus.objects.get(status = cd['meet_status']),
            meet_status_defenition = cd['meet_status_defenition'],
            meetemp_status = MeetEmpStatus.objects.get(status = cd['meetemp_status']),
            meetemp_status_defenition = cd['meetemp_status_defenition']).save()
            return redirect('/jobseek')
        else:
            messages.error(request, 'Заявка уже существует или введены неверные данные')
    form = AddJobSeek()
    content = {
        "form":form
    }
    return render(request, 'start/add_candidate.html', content)

@login_required(login_url='/login')
def changeCandidate(request,pk):
    candidate = Candidate.obgects.get(pk = pk)
    if request.method == 'POST':
        form = AddCandidateForm(request.POST,request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            candidate.name=cd['name']
            candidate.phone=cd['phone']
            candidate.email=cd['email']
            candidate.sex=cd['sex']
            candidate.position = cd['position']
            candidate.photo=cd['photo']
            candidate.birthdate=cd['birthdate']
            candidate.cv=cd['cv']
            candidate.save()
            return redirect('cercandidate/'+pk)
        else:
            messages.error(request, 'Кандидат уже существует или введены неверные данные')
    form = AddCandidateForm(initial={
        "name": candidate.name,
        "phone": candidate.phone,
        "email": candidate.email,
        "sex": candidate.sex,
        "position" : candidate.position,
        "photo": candidate.phone,
        "birthdate": candidate.birthdate,
        "cv": candidate.cv
    })
    content = {
        "form": form,
        "candidate": candidate
    }
    return render(request, 'startchangeCandidate.html',content)

@login_required(login_url='/login')
def changeJob(request,pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            job.name=cd['name']
            job.salary=cd['salary']
            job.expirence=cd['expirence']
            job.employment=cd['employment']
            job.definition=cd['definition']
            job.status=cd['status']
            job.save()
            return redirect('cerjob/'+pk)
        else:
            messages.error(request, 'Введены неверные данные')
    form = AddJobForm(initial={
        "name" : job.name,
        "salary" : job.salary,
        "expirence" : job.expirence,
        "employment" : job.employment,
        "definition" : job.definition,
        "status" : job.status,
    })
    content = {
        "form": form,
        "candidate": job
    }
    return render(request, 'start/changeJob.html',content)

@login_required(login_url='/login')
def changeJobSeek(request,pk):
    jobSeek = JobSeek.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddJobSeek(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            jobSeek.offer = cd['offer']
            jobSeek.offer_definition = cd['offer_definition']
            jobSeek.release_date = cd['release_date']
            jobSeek.denial_status = DenialStatus.objects.get(status = cd['denial_status'])
            jobSeek.call_status = CallStatus.objects.get(status = cd['call_status'])
            jobSeek.call_status_defenition = cd['call_status_defenition']
            jobSeek.test_status = TestStatus.objects.get(status = cd['test_status'])
            jobSeek.test_status_defenition = cd['test_status_defenition']
            jobSeek.meet_status = MeetStatus.objects.get(status = cd['meet_status'])
            jobSeek.meet_status_defenition = cd['meet_status_defenition']
            jobSeek.meetemp_status = MeetEmpStatus.objects.get(status = cd['meetemp_status'])
            jobSeek.meetemp_status_defenition = cd['meetemp_status_defenition']
            jobSeek.save()
            return redirect('cerjobSeek/'+pk)
        else:
            messages.error(request, 'Введены неверные данные')
    form = AddJobSeek(initial={
        "job": jobSeek.job,
        "candidate":jobSeek.candidate,
        "offer":jobSeek.offer,
        "offer_definition":jobSeek.offer_definition,
        "release_date":jobSeek.release_date,
        "denial_status":jobSeek.denial_status,
        "call_status":jobSeek.call_status,
        "call_status_defenition":jobSeek.call_status_defenition,
        "test_status":jobSeek.test_status,
        "test_status_defenition":jobSeek.test_status_defenition,
        "meet_status":jobSeek.meet_status,
        "meet_status_defenition":jobSeek.meet_status_defenition,
        "meetemp_status":jobSeek.meetemp_status,
        "meetemp_status_defenition":jobSeek.meetemp_status_defenition
    })
    content = {
        "form": form,
        "candidate": jobSeek
    }
    return render(request,'start/changeJobSeek.html',content)

@login_required(login_url='/login')
def get_cv(request,pk):
    document = Candidate.objects.get(pk = pk)
    try:
        from django.http import FileResponse
        return FileResponse(open(os.path.join(os.path.dirname(os.path.dirname(__file__)),document.document.name), 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        from django.http import Http404
        raise Http404()