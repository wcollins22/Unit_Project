from django import forms 

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=50)

class SearchForm(forms.Form):
    name = forms.CharField(max_length=30)
   