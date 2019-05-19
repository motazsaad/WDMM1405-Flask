from flask import Flask
from flask_restful import Resource, Api

# pip install Flask-RESTful
app = Flask(__name__)
# create API for my app
api = Api(app)

temperature = {'Gaza': 23, 'Tripoli': 26, 'Alexandria': 24,
               'Izmir': 22, 'Istanbul': 19, 'Athens': 20, 'Napoli': 20,
               'Genova': 18, 'Marseille': 17, 'Barcelona': 18,
               'Casablanca': 20, 'Oran': 24, 'Bizerte': 17}


class Weather(Resource):
    def get(self, city):
        return {city: temperature.get(city, '')}


api.add_resource(Weather, '/weather/<city>')

if __name__ == '__main__':
    app.run()
