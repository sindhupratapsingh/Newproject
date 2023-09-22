from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
import datetime
# Create your views here.
def home(request):
    return render(request,'home.html') 





def user_data(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'submitted_data.html', {'name': name, 'email': email})
    else:
        form = UserForm()
    return render(request, 'user_data_form.html', {'form': form})






def current_datetime(request):
    current_time = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_time': current_time})


