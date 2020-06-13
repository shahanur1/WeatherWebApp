from django.shortcuts import render
from django.contrib import messages 


import requests
from datetime import datetime

# models
from .models import City

# forms
from .forms import CityForm

api = '9ea9cea81a5388aec87a14d0f26a68a0'
# Create your views here.
def home(request):
    # city_name = 'New Delhi'
    form = CityForm()
    load_time = datetime.now()
    try:
        city_name = request.GET['name']
        url =   f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api}"
        data = requests.get(url).json()
        fetch_time = datetime.now()

        last_update_time = (fetch_time-load_time).seconds // 60

        weather_data = {
            'weather' : data['weather'][0]['description'],
            'icon'  : data['weather'][0]['icon'],
            'temp'  : data['main']['temp'],
            'pressure' : data['main']['pressure'],
            'humidity' : data['main']['humidity'],
            'city_name' : city_name,
            'fetch_time': fetch_time,
            'load_time' : load_time,
            'last_update_time' : last_update_time    
        }
        context = {
            'data' : weather_data,
            'form':form
        }
    except:
        context = {'form':form}
        
        # for first time load of the page
        if request.GET.get('name', False):
            city_name = request.GET['name']
            messages.warning(request, f'Cannot retrieve data for {city_name}')
    
    template_name = 'weather/index.html'
    return render(request, template_name, context)