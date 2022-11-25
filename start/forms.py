from django import forms
from django.contrib.auth.models import User
from .models import Job

class AddCandidateForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    phone = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    sex = forms.CharField(widget=forms.TextInput)
    photo = forms.FileField(widget=forms.FileInput)
    birthdate = forms.DateField(widget=forms.DateInput)
    cv = forms.FileField(widget=forms.FileInput)
    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'sex', 'photo', 'birthdate', 'cv')

class AddJobForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    salary = forms.IntegerField(widget=forms.NumberInput)
    expirence = forms.IntegerField(widget=forms.NumberInput)
    employment = forms.CharField(widget=forms.TextInput)
    definition = forms.CharField(widget=forms.TextInput)

    # class Meta:
    #     model = Job
    #     fields = ('name', 'salary', 'expirence', 'employment', 'definition')

class AddJobForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    salary = forms.IntegerField(widget=forms.NumberInput)
    expirence = forms.IntegerField(widget=forms.NumberInput)
    employment = forms.CharField(widget=forms.TextInput)
    definition = forms.CharField(widget=forms.TextInput)
        # class Meta:
        #     model = Job
        #     fields = ('name', 'salary', 'expirence', 'employment', 'definition', 'id_status', 'user')