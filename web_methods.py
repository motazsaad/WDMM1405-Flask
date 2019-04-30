from flask import Flask
from flask import render_template
from flask import request

# the name of the module for configuration
app = Flask(__name__)


# view functions
# View functions are mapped to one or more route URLs so that Flask knows
# what logic to execute when a client requests a given URL.
# Decorators (@app.route) are used to register
# functions as callbacks for certain events
@app.route('/')
@app.route('/index')
@app.route('/main')
# associate / /index and /main with this function
def hello_world():
    message = 'Hello World!'
    # we are in web not in CLI, so use <br> for new line :)
    message += '<br>App name: ' + app.name
    return message


# Variable Rules
# method 1 to get parameter
@app.route('/hello/<name>')
def hello_name(name):
    # to call /hello/Ahmed
    return 'Hello {}!'.format(name)


# method 2 to get parameter
@app.route('/greeting')
def greet_name():
    name = request.args.get('name')
    # to call /greeting?name="Ahmed"
    return 'Hello {}!'.format(name)


# method 3
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    # to call /post/10
    return 'Post %d' % post_id


@app.route('/hello2')
def hello2():
    name = request.args.get('name')
    return render_template('hello.html', name=name)


@app.route('/sum')
def add():
    x = request.args.get('x')
    y = request.args.get('y')
    return 'the sum of {} and {} is {}'.format(x, y, int(x) + int(y))


if __name__ == '__main__':
    app.run(debug=True)
