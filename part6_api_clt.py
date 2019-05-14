import requests

r = requests.get(url='http://127.0.0.1:5000/')
print(r)
response = r.json()
print(response['message'])

r = requests.get(url='http://127.0.0.1:5000/mult/10')
print(r)
response = r.json()
print(response['result'])

r = requests.get(url='http://127.0.0.1:5000/hello')
print(r)
response = r.json()
print(response)

r = requests.post(url='http://127.0.0.1:5000/hello', data='Hi')
print(r)
response = r.json()
print(response)
