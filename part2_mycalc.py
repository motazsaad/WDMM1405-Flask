from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add')
def add():
    x = request.args.get('x')
    y = request.args.get('y')
    total = int(x) + int(y)
    return '<h1> result = {} </h1>'.format(total)


@app.route('/add2')
def add2():
    x = request.args.get('x')
    y = request.args.get('y')
    total = int(x) + int(y)
    return render_template('add2.html', x=x, y=y, total=total)


if __name__ == '__main__':
    app.run(debug=True)
