import requests

r = requests.get(url='http://127.0.0.1:5000/')
print(r)
response = r.json()
print(response['message'])

r = requests.post(url='http://127.0.0.1:5000/', json={'greeting': 'Hi'})
print(r)
response = r.json()
print(response)

r = requests.get(url='http://127.0.0.1:5000/mult/32')
print(r)
response = r.json()
print(response['result'])
