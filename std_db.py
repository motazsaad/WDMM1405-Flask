import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello word!'


@app.route('/std_db')
def std_db():
    # step 1: connect to db
    conn = sqlite3.connect('std3.sqlite')
    # step2: define cursor
    cur = conn.cursor()
    # step3: execute SQL statment
    # SQL query: select <field name(s)> from table
    # select std_id, dept from std_info
    cur.execute('select * from std_info')
    # step 4: fetch records
    rows = cur.fetchall()
    # print(rows)
    return render_template('std_db3.html', rows=rows)


@app.route('/std')
def std():
    student_id = request.args.get('stdid')
    # step 1: connect to db
    conn = sqlite3.connect('std3.sqlite')
    # step2: define cursor
    cur = conn.cursor()
    # step3: execute SQL statement
    # SQL query: select <field name(s)> from table
    # select std_id, dept from std_info
    cur.execute('select * from std_info where std_id={}'.format(student_id))
    # step 4: fetch records
    rows = cur.fetchall()
    # print(rows)
    return render_template('std_db3.html', rows=rows)


if __name__ == '__main__':
    app.run()
