from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/contact')
def contact():
    cont = 'msaad@iugaza.edu.ps'
    return render_template('contact.html', abc=cont)


@app.route('/greeting')
def greeting():
    name = request.args.get('user')
    return render_template('greeting.html', name=name)


@app.route('/add')
def add():
    x = request.args.get('x')
    y = request.args.get('y')
    total = int(x) + int(y)
    return render_template('myadd.html',
                           x=x, y=y, total=total)


if __name__ == '__main__':
    app.run(debug=True)
