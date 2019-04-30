# 1. import flask
from flask import Flask, render_template

# 2. create flask object
app = Flask('myApp')


# 3. create web page
@app.route('/')
# 4. define a function for the web page
def home():
    return '<h1> hello from flask </h1>'


@app.route('/support')
def support():
    return '<h2> how can I help you </h2>'


@app.route('/help')
def helpme():
    contact = 'msaad@iug.edu.ps'
    return render_template('help.html', contact=contact)


# 5. run in main
if __name__ == '__main__':
    app.run()

'''
http messages code 
200 OK 
404 not found 
500 server error 
'''
