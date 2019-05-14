from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello World!'})


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        some_data = request.data
        return jsonify({'you sent': some_data})
    else:
        return jsonify({'message': 'Hello World!'})


@app.route('/mult/<int:num>')
def mult(num):
    return jsonify({'result': num * num})


if __name__ == '__main__':
    app.run(debug=True)
