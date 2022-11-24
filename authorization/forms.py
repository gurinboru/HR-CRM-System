from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control login_signin', 'id':"floatingInput", "placeholder":"Login"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control password_signin', "id":"floatingPassword", "placeholder":"Password"}))

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={ "class":"form-control reg_middle",  "minlength":"6", "id":"validationCustom03", "placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ "class":"form-control", "id":"validationCustom04", "placeholder":"Confirm password"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "pattern":"\D[^А-Яа-я ]{1,20}", "id":"validationCustom01", "placeholder":"loginexample" }))
    class Meta:
        model = User
        fields = ('username', 'email')