from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello from flask'


@app.route('/appname')
def get_name():
    return app.name


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome_page.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

'''
http messages code 
200 OK 
404 not found 
500 server error 
'''
