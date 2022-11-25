from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('registration', views.registration_user),
    path('logout', views.user_logout),
]
