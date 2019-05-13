import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return 'hello from flask'


@app.route('/greeting', methods=['GET', 'POST'])
def greet():
    message = None
    if request.method == 'POST':
        name = request.form['std_name']
        if name:
            message = 'Hello ' + name
        else:
            message = 'Hello student'

    return render_template('mygreeting.html', message=message)


@app.route('/students')
def std():
    # nested dictionary
    students = {
        '120191122': {'name': 'ahmed', 'dept': 'MM'},
        '120192233': {'name': 'Mohammad', 'dept': 'MM'},
        '220192233': {'name': 'Noor', 'dept': 'Mobi'}
    }
    return render_template('students.html', students=students)


@app.route('/list_students')
def list_std():
    # nested dictionary
    students = {
        '120191122': {'name': 'Ahmed', 'dept': 'MM'},
        '120192233': {'name': 'Mohammad', 'dept': 'MM'},
        '120193344': {'name': 'Abderrahman', 'dept': 'Commerce'}

    }
    return render_template('list_students.html', students=students)


@app.route('/std_db')
def std_db():
    conn = sqlite3.connect('students.sqlite')
    cur = conn.cursor()
    cur.execute('''select *  from student_info''')
    rows = cur.fetchall()
    # print(rows)

    return render_template('std_db.html', rows=rows)


if __name__ == '__main__':
    app.run()
