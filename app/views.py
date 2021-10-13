from django.shortcuts import render
from app.forms import StudentForm

# Create your views here.

def home(request):
    form = StudentForm()