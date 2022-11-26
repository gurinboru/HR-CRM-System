
from django.urls import path
from start import views

urlpatterns = [
    path('', views.start),
    path('candidates', views.getCandidates),
    path('add_candidate', views.addCandidate),
    path('change_candidate/<int:pk>', views.changeCandidate),
    path('change_job/<int:pk>', views.changeJob),
    path('change_jobseek/<int:pk>', views.changeJobSeek),
    path('add_jobseek', views.addJobSeek),
    path('jobs', views.getJob),
    path('jobseek', views.getJobSeek),
    path('add_job', views.addJob),
    path('cerjobseek/<int:pk>', views.getCerJobSeek, name='cerjobseek'),
    path('cercandidate/<int:pk>', views.getCerCandidate, name='cercandidate'),
    path('cerjob/<int:pk>', views.getCerJob, name='cerjob'),
    path('candidates', views.getCandidates),
    path('jobs', views.getJob),
    path('jobseek', views.getJobSeek),
    path('cercandidate/get_cv/<int:pk>', views.get_cv),
    path('parseHTML', views.parseHTML)
]