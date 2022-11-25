from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={ "class":"input"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ "class":"input"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"input"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"input"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"input"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"input"}))
    class Meta:
        model = User
        fields = ('username', 'email',"first_name","last_name"
                  )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
