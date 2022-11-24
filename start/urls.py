
from django.urls import path

from start import views

urlpatterns = [
    path('', views.start),
    path('login', views.login),
    path('registration', views.registration_user)
]