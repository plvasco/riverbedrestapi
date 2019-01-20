
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather?appid=32fda3c5564acd6e8e5c4a513b8350f5&q=London"
url2 = "http://api.openweathermap.org/data/2.5/weather?appid=32fda3c5564acd6e8e5c4a513b8350f5&q=Houston"

#city = input ("City Name  :")

json_data1 = requests.get(url1).json()
json_data2 = requests.get(url2).json()


print(json_data1)
print(json_data2)



