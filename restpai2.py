
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather?appid=32fda3c5564acd6e8e5c4a513b8350f5&q=London"


#city = input ("City Name  :")

json_data = requests.get(url1).json()

print(json_data)



