
from django.urls import path

from start import views

urlpatterns = [
    path('', views.start),
    path('candidates', views.getCandidates),
    path('add_condidate', views.addCandidate),
    path('jobs',views.getJob),
    path('jobseek',views.getJobSeek),
    path('cerjobseek/<int:pk>', views.getCerJobSeek),
    path('cercandidate/<int:pk>', views.getCerJobSeek),
    path('cerjob/<int:pk>', views.getCerJobSeek),
    path('candidates', views.getCandidates),
    path('jobs', views.getJob),
    path('jobseek', views.getJobSeek),

]