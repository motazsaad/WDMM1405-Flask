from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/main')
def home():
    return 'hello from flask'


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page2')
def page2():
    mylist = [3, 5, 6, 8, 10, 13, 45, -20]
    return render_template('page2.html', mylist=mylist)


if __name__ == '__main__':
    app.run()
