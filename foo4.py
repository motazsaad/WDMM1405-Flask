from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return 'hello from flask'


@app.route('/add', methods=['GET', 'POST'])
def add():
    result = None
    if request.method == 'POST':
        n1 = request.form['num1']
        op = request.form['op']
        n2 = request.form['num2']
        try:
            result = eval('{}{}{}'.format(n1, op, n2))
        except BaseException as error:
            result = 'error: {}'.format(error)

    return render_template('add002.html', result=result)


@app.route('/page2')
def page2():
    return render_template('page_0002.html')


@app.route('/page3')
def page3():
    # nested dictionary
    students = {
        '120191122': {'name': 'ahmed', 'dept': 'MM'},
        '120192233': {'name': 'mohammed', 'dept': 'MM'},
        '120193344': {'name': 'Khaild', 'dept': 'Mobi'}
    }
    return render_template('page_0003.html', students=students)


if __name__ == '__main__':
    app.run()
