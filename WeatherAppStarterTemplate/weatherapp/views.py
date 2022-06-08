from django.shortcuts import get_object_or_404, render, redirect
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages
from weatherapp.models import City

def home(request):
    API_KEY = config('API_KEY')
    u_city = request.GET.get('name')
    if u_city : 
        url = f"https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.ok:
            content = response.json()
            r_city = content['name']
            if City.objects.filter(name=r_city):
                messages.warning(request, 'City already exists!')
            else:
                City.objects.create(name=r_city)
                messages.success(request, 'City created')
        else:
            messages.error(request, 'There is no city!')
        return redirect('home')
    
    
    
    city_data = []
    cities = City.objects.all()
    for city in cities:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        content = response.json()
        
        data ={
            'city' : city,
            'temp' : content['main']['temp'],
            'icon' : content['weather'][0]['icon'],
            'desc' : content['weather'][0]['description'],
            
        }
        city_data.append(data)
        

    context = {
        'city_data': city_data,
    }
    return render(request, 'weatherapp/home.html', context)

def delete_city(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.success(request, 'City deleted successfully')
    return redirect('home')
