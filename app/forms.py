from django import forms 
from app.models import Student

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=100)
    dream = forms.CharField(max_length=100)
    job = forms.CharField(max_length=50)
    hometown = forms.CharField(max_length=50)