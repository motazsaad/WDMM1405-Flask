from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
# {'city': 'temp'}
# temperature = {'Gaza': 23, 'Tripoli': 26, 'Alexandria': 24,
#                'Izmir': 22, 'Istanbul': 19, 'Athens': 20,
#                'Napoli': 20, 'Genova': 18, 'Marseille': 17,
#                'Barcelona': 18, 'Casablanca': 20, 'Oran': 24,
#                'Bizerte': 17, 'Rafah': 23, 'Khanyounis': 30}

weather_data = {
    'Gaza': {'temp': 19, 'wind': 16, 'humidity': 80},
    'Khanyounis': {'temp': 30, 'wind': 10, 'humidity': 20},
    'Rafah': {'temp': 23, 'wind': 10, 'humidity': 80}
}


class Weather(Resource):
    def get(self, city):
        weather_city = weather_data.get(city)
        return {city: weather_city}


api.add_resource(Weather, '/weather/<city>')

if __name__ == '__main__':
    app.run()
