from django.shortcuts import render
from weather_project.local_settings import API_KEY
import urllib.request
import json

def index(request):
    return render(request, "main/index.html")

def weather_data(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        if city:
            source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}').read()
            list_of_data = json.loads(source)
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate":  str(list_of_data['coord']['lat']) + ', ' + str(list_of_data['coord']['lon']),
                "temp":  str(list_of_data['main']['temp']) + '°C',
                "pressure":  str(list_of_data['main']['pressure']),
                "humidity":  str(list_of_data['main']['humidity']),
                "main":  str(list_of_data['weather'][0]['main']),
                "description":  str(list_of_data['weather'][0]['description']),
                "icon":  list_of_data['weather'][0]['icon'],
            }
        else:
            data = {"message": "Please enter a city.."}
    else:
        data = {}
    return render(request, "main/weather.html", data)

def cats_data(request):
    return render(request, "main/cats.html")

def cats_n_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        if city:
            source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}').read()
            list_of_data = json.loads(source)
            city = city + ': '
            temperature = str(round(list_of_data['main']['temp'])) + '°C'
            data = {
                "city": city, 
                "temp": temperature
                }
        else:
            data = {"message": "Please enter a city.."}
    else:
        data = {}
    return render(request, "main/cats_n_weather.html", data)
