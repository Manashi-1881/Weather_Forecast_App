import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=617f5f49dbdd25164a7cd3800aecc7d4'

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()

    form = CityForm()
    weather = []  # request the API data and convert the JSON to Python data types
    li = City.objects.all()

    for city in li:

        city_weather = requests.get(url.format(city.name)).json()  # request the API data and convert the JSON to Python data types

        w = {
            'city': city.name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather.append(w)
    context = {'weather' : weather, 'form': form}

    return render(request, 'weather.html',context)
