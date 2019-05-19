from flask import Flask, jsonify, request

app = Flask(__name__)
# {'city': 'temperature'}
weather = {'Gaza': 21, 'Istanbul': 19, 'Cairo': 25,
           'Paris': 17, 'Berlin': 20}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        message = 'hello {}!'.format(name)
        return jsonify({'message': message})
    else:  # GET
        return jsonify({'message': 'Hello from Flask API'})


# provide weather API
@app.route('/weather', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        city = data.get('city')
        print(city)
        temperature = weather.get(city)
        print(temperature)
        return jsonify({'temperature': temperature})
    else:  # GET
        return jsonify({'temperature': weather})


if __name__ == '__main__':
    app.run()
