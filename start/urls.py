
from django.urls import path
from start import views

urlpatterns = [
    path('', views.start),
    path('candidates', views.getCandidates),
    path('add_candidate', views.addCandidate),
    path('add_jobseek', views.addJobSeek),
    path('jobs',views.getJob),
    path('jobseek',views.getJobSeek),
    path('add_job', views.addJob),
    path('cerjobseek/<int:pk>', views.getCerJobSeek),
    path('cercandidate/<int:pk>', views.getCerCandidate),
    path('cerjob/<int:pk>', views.getCerJob),
    path('candidates', views.getCandidates),
    path('jobs', views.getJob),
    path('jobseek', views.getJobSeek),
    path('get_cv/<int:pk>',views.get_cv)
]