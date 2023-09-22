from django.shortcuts import render
from django.http import HttpResponse

from app.forms import UserForm
from datetime import datetime


# Create your views here.
def home(request):
    




    current_datetime = datetime.now() 
    return render(request,'home.html', {'current_datetime':current_datetime}) 

def about(request):
    return render(request,'about.html') 

def user_data_form(request):
    return render(request,'user_data_form.html') 

