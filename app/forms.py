from django import forms 
from app.models import Student

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=50)
   