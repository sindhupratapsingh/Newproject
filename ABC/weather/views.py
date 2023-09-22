from django.shortcuts import render

from .api import get_weather_data

def home(request):
    city = 'Lucknow'  
    weather_data = get_weather_data(city)
    temperature = weather_data['current']['temp_c']
    conditions = weather_data['current']['condition']['text']
    
    context = {'city': city, 'temperature': temperature, 'conditions': conditions}
    return render(request, 'home.html', context)

