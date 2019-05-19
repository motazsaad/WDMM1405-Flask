from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        message = 'Hello {}!'.format(name)
        return jsonify({'message': message})
    else:  # GET
        return jsonify({'message': 'hello from flask API!'})


# {'city': 'temp'}
temperature = {'Gaza': 23, 'Tripoli': 26, 'Alexandria': 24,
               'Izmir': 22, 'Istanbul': 19, 'Athens': 20,
               'Napoli': 20, 'Genova': 18, 'Marseille': 17,
               'Barcelona': 18, 'Casablanca': 20, 'Oran': 24,
               'Bizerte': 17, 'Rafah': 23, 'Khanyounis': 30}


@app.route('/weather/<city>')
def get_temp(city):
    temp = temperature.get(city)
    return jsonify({'temp': temp})


if __name__ == '__main__':
    app.run()
