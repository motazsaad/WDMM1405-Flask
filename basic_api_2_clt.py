# client in python
import requests

# pip install requests

'''
from flask import request ===> used in server side 
import requests ==> used in client side 

'''

r = requests.get(url='http://127.0.0.1:5000/')
print(r)
print(r.status_code)
print(r.json())
result = r.json()
print(result['message'])
print(result.get('message'))
print('-------------------------')

r = requests.post(url='http://127.0.0.1:5000/',
                  json={'name': 'Ahmed'})
print(r.status_code)
print(r.json().get('message'))

print('-------------------------')
print('Call weather service')
city = 'Istanbul'
r = requests.post(url='http://127.0.0.1:5000/weather',
                  json={'city': city})
print('the temperature in {} is {}'.format(city, r.json().get('temperature')))

r = requests.get(url='http://127.0.0.1:5000/weather')
for city, temp in r.json().get('temperature').items():
    print('City: {}\t Temperature: {}'.format(city, temp))
