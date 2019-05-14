from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

temperature = {'Gaza': 23, 'Tripoli': 26, 'Alexandria': 24,
               'Izmir': 22, 'Istanbul': 19, 'Athens': 20, 'Napoli': 20,
               'Genova': 18, 'Marseille': 17, 'Barcelona': 18,
               'Casablanca': 20, 'Oran': 24, 'Bizerte': 17}


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World!'}

    def post(self):
        some_data = request.get_json()
        return {'you sent': some_data}


class Weather(Resource):
    def get(self, city):
        return {city: temperature.get(city, '')}


api.add_resource(HelloWorld, '/')
api.add_resource(Weather, '/weather/<city>')

if __name__ == '__main__':
    app.run()
