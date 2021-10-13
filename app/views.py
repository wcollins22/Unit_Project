from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from app.models import Student
from app.forms import ProfileForm


def profile_function(request):
    form = ProfileForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        

        return render(request, "profiles.html", {"form":form, "name":name})
    else:
        return render(request, "profiles.html",)
