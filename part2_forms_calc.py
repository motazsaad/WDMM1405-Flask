from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sum')
def sum_numbers():
    x1 = request.args.get('x')
    y1 = request.args.get('y')
    return '<h2> {} + {} = {} </h2>'.format(x1, y1, int(x1) + int(y1))


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    l = 'this is my calculator'.split()
    result = None  # when the method is GET
    if request.method == 'POST':
        if not request.form['num1'] and not request.form['num2'] \
                and not request.form['op']:
            result = 'please fil the form'
            # print(result)
        else:
            try:
                n1 = request.form['num1']
                n2 = request.form['num2']
                op = request.form['op']
                # print(n1, op, n2)
                result = eval('{}{}{}'.format(n1, op, n2))
                # print(result)
            except BaseException as error:
                result = 'error: {}'.format(error)
                # print(result)
    return render_template('calculator.html', result=result, l=l)


@app.route('/calculator2', methods=['GET', 'POST'])
def calculator2():
    result = ''
    n1 = ''
    n2 = ''
    op = ''
    if request.method == 'POST':
        n1 = request.form['num1']
        n2 = request.form['num2']
        op = request.form['op']
        if n1 and n2:
            try:
                result = eval('{}{}{}'.format(n1, op, n2))
                print(result)
            except BaseException as error:
                result = 'error: {}'.format(error)
                print(result)
        else:
            result = 'please fill the form'
    return render_template('calculator2.html', n1=n1, op=op, n2=n2, result=result)


if __name__ == '__main__':
    app.run(debug=True)
