import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/list_std')
def list_std():
    # nested dictionary
    students = {
        '120191122': {'name': 'Ahmed', 'dept': 'MM'},
        '120192233': {'name': 'Mohammad', 'dept': 'MM'},
        '220193344': {'name': 'Fatima', 'dept': 'MM'}
    }
    return render_template('list_std007.html', students=students)


@app.route('/std_db')
def std_db():
    # step 1: connect to db
    conn = sqlite3.connect('std1.sqlite')
    # step 2: create a cursor
    cur = conn.cursor()
    # step 3: execute SQL statement
    cur.execute('''select * from std_info''')
    # step 4: fetch
    rows = cur.fetchall()
    # print(rows)
    return render_template('std_db07.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
