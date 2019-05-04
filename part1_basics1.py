# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    # return a string
    return "Hello, World!"


@app.route('/welcome')
def welcome():
    # render a template
    return render_template('welcome.html')


@app.route('/steps')
def steps():
    # render a template
    return render_template('steps.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
