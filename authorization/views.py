import django
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    django.contrib.auth.login(request, user)
                    return redirect('/candidates')
                else:
                    messages.error(request, 'Disabled account')
                    # return render(request, 'login/login.html', context={"form": form})
            else:
                messages.error(request, 'Введен неверный логин или пароль')
            return render(request, 'authentication/login.html', context={"form": form})
    form = LoginForm()
    return render(request, 'authentication/login.html', context={"form": form})


def registration_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_active = True
            new_user.save()
            login(request, new_user)
            return render(request, 'start/candidates.html')
        else:
            messages.error(request, 'Аккаунт уже существует или введены неверные данные')
        return render(request, 'authentication/registration.html', context={"form": user_form})
    user_form = UserRegistrationForm()
    return render(request, 'authentication/registration.html', context={"form": user_form})


def user_logout(request):
    logout(request)
    form = LoginForm()
    return render(request, 'authentication/login.html', context={"form": form})
