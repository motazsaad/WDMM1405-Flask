import requests

city = 'Tripoli'
r = requests.get(url='http://127.0.0.1:5000/weather/{}'.format(city))
print('temp in {} is {}'.format(city, r.json().get(city)))
