import requests
from pprint import pprint

API_key='a78bd62e0550be6117da77f724ceba99'

city=input("Enter a City: ")

base_url="http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)