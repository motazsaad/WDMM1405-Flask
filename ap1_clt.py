import requests

# pip install requests

r = requests.get(url='http://127.0.0.1:5000/')
print(r)
print(r.status_code)
print(r.text)
result = r.json()
print(result['message'])
print('------------------------------')
r = requests.post(url='http://127.0.0.1:5000/',
                  json={'message': 'Hello API'})
print(r.status_code)
result = r.json()
print(result.get('you sent'))

print('---------------------')

r = requests.post(url='http://127.0.0.1:5000/weather',
                  json={'city': 'Gaza'})
print(r.status_code)
result = r.json()
print(result.get('temperature'))

print('get all cities')
r = requests.get(url='http://127.0.0.1:5000/weather')
print(r.status_code)
result = r.json()
print(result)
