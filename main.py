import requests
import pprint

API_Key = "c739cf1b93fbe41d1b7682c8a7af9d02"

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" +API_Key+"&q="+city

weather_data = requests.get(base_url).json()
pp=pprint.PrettyPrinter(indent=3)
pp.pprint(weather_data)