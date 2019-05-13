from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return 'hello from flask'


@app.route('/add')
def add():
    x = request.args.get('x')
    y = request.args.get('y')
    total = int(x) + int(y)
    return '{} + {} = {}'.format(x, y, total)


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    result = None
    if request.method == 'POST':
        n1 = request.form['num1']
        op = request.form['op']
        n2 = request.form['num2']
        try:
            result = eval('{}{}{}'.format(n1, op, n2))
        except BaseException as error:
            result = 'error: {}'.format(error)

    return render_template('calc001.html', result=result)


@app.route('/page1')
def page1():
    # nested dict
    students = {
        '120191122': {'name': 'ahmed', 'dept': 'MM'},
        '120193344': {'name': 'mohammed', 'dept': 'MM'},
        '220194455': {'name': 'Fatima', 'dept': 'MM'}
    }
    return render_template('page001.html', students=students)


@app.route('/page2')
def page2():
    return render_template('page002.html')


if __name__ == '__main__':
    app.run()
