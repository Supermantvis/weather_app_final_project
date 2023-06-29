import urllib.request
import json


source = urllib.request.urlopen(
    'https://openweathermap.org/data/2.5/weather?q=' + 
    'kaunas' + 
    '&units=metric&appid=f6e0ee3f7639429700d8bf44f5d8d5c2').read()
list_of_data = json.loads(source)
data = {
    "country_code": str(list_of_data['sys']['country']),
    "coordinate":  str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
    "temp":  str(list_of_data['main']['temp']) + '°C',
    "pressure":  str(list_of_data['main']['pressure']),
    "humidity":  str(list_of_data['main']['humidity']),
    "main":  str(list_of_data['weather'][0]['main']),
    "description":  str(list_of_data['weather'][0]['description']),
    "icon":  list_of_data['weather'][0]['icon'],
}
print(data)
