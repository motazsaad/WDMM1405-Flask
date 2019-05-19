import requests

city = 'Gaza'
r = requests.get(url='http://127.0.0.1:5000/weather/{}'.format(city))
result = r.json().get(city)
# print(result)
print('city: {}, temp: {}, wind: {}, humidity: {}'.format(city, result.get('temp'), result.get('wind'),
                                                          result.get('humidity')))
