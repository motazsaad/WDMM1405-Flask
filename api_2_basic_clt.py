# client
import requests

# pip install requests

'''
from flask import request ====> request in server side
import requests ===> request in client slide  


'''

r = requests.get(url='http://127.0.0.1:5000/')
print(r)
print(r.status_code)
print(r.json())
result = r.json()
print(result['message'])
print(result.get('message'))

r = requests.post(url='http://127.0.0.1:5000/',
                  json={'name': 'Ahmed'})
print(r.json().get('message'))

city = 'Barcelona'
r = requests.get(url='http://127.0.0.1:5000/weather/{}'.format(city))
print('the temp in {} is {}'.format(city, r.json().get('temp')))

print(requests.get(url='http://127.0.0.1:5000/weather/Rafah').json())
