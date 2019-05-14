from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World!'}

    def post(self):
        some_data = request.get_json()
        return {'you sent': some_data}


class Mult(Resource):
    def get(self, num):
        return {'result': num * num}


api.add_resource(HelloWorld, '/')
api.add_resource(Mult, '/mult/<int:num>')

if __name__ == '__main__':
    app.run()
