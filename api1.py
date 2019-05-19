from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        some_json = request.data
        return jsonify({'you sent': some_json})
    else:
        return jsonify({'message': 'Hello Word'})


@app.route('/weather', methods=['GET', 'POST'])
def get_weather():
    weather = {
        'Gaza': 25, 'Istanbul': 20, 'Dubai': 30
    }
    if request.method == 'POST':
        city = request.get_json().get('city')
        print(city)
        return jsonify({'temperature': weather.get(city, '')})
    else:
        return jsonify({'all_cities': weather})


if __name__ == '__main__':
    app.run()
