import requests
import json

my_link = ['http://www.google.com', 'http://www.yahoo.com']
my_responses = []
for link in my_link:
    payload = requests.get(link).json()
    print('got response from {}'.format(link))
    my_responses.append(payload)
    print(payload)