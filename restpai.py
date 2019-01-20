import requests
from pprint import pprint
 
# API KEY
API_key = "32fda3c5564acd6e8e5c4a513b8350f5"
 
# This stores the url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# This will ask the user to enter city ID
city_id = input("Enter a city ID : ")
 
# This is final url. This is concatenation of base_url, API_key and city_id
Final_url = base_url + "appid=" + API_key + "&id=" + city_id
 
# this variable contain the JSON data which the API returns
weather_data = requests.get(Final_url).json()
 
# JSON data is difficult to visualize, so you need to pretty print 
pprint(weather_data)