from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    desc = request.args.get('abc')
    return render_template('about.html', desc=desc)


@app.route('/calc')
def calc():
    x = request.args.get('x')
    y = request.args.get('y')
    total = int(x) + int(y)
    return render_template('mycalc.html', x=x, y=y,
                           total=total)


if __name__ == '__main__':
    app.run(debug=True)
