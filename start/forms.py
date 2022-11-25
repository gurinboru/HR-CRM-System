from django import forms
from django.contrib.auth.models import User
from django.forms import NumberInput

from .models import *

class AddCandidateForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"ФИО"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"89........."}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"example@mail.ru"}))
    sex = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Муж/жен"}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "placeholder":"Фото"}))
    birthdate = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class":"form-control", "placeholder":"01.01.1999"}))
    cv = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))
    class Meta:
        model = Candidate
        fields = ('username', 'phone', 'email', 'sex', 'photo', 'birthdate', 'cv')

class AddJobForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    salary = forms.IntegerField(widget=forms.NumberInput)
    expirence = forms.IntegerField(widget=forms.NumberInput)
    employment = forms.CharField(widget=forms.TextInput)
    definition = forms.CharField(widget=forms.TextInput)
    status = forms.ChoiceField(choices = StatusJob.CHOICES)
        # class Meta:
        #     model = Job
        #     fields = ('name', 'salary', 'expirence', 'employment', 'definition', 'id_status', 'user')

class AddJobSeek(forms.Form):
    job = forms.ModelChoiceField(queryset=Job.objects.all())
    candidate = forms.ModelChoiceField(queryset=Candidate.objects.all())
    offer = forms.IntegerField(widget=forms.NumberInput)
    offer_definition = forms.CharField(widget=forms.TextInput)
    release_date = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class":"form-control", "placeholder":"01.01.1999"}))
    denial_status = forms.ChoiceField(choices = DenialStatus.CHOICES)
    call_status = forms.ChoiceField(choices = CallStatus.CHOICES)
    call_status_defenition = forms.CharField(widget=forms.TextInput)
    test_status = forms.ChoiceField(choices = TestStatus.CHOICES)
    test_status_defenition = forms.CharField(widget=forms.TextInput)
    meet_status = forms.ChoiceField(choices = MeetStatus.CHOICES)
    meet_status_defenition = forms.CharField(widget=forms.TextInput)
    meetemp_status = forms.ChoiceField(choices = MeetEmpStatus.CHOICES)
    meetemp_status_defenition = forms.CharField(widget=forms.TextInput)