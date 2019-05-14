import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/std_db')
def std_db():
    # step1 : connect to db
    conn = sqlite3.connect('std2.sqlite')
    # step2 : define cursor
    cur = conn.cursor()
    # step3: execute SQL statement
    # select <field name(s)> from table
    # select std_id, dept from std_info
    cur.execute('''select * from std_info''')
    # step4: fetch records
    rows = cur.fetchall()
    # print(rows)

    return render_template('std08.html', rows=rows)


@app.route('/std_id')
def std_id():
    student_id = request.args.get('stdid')
    # step1 : connect to db
    conn = sqlite3.connect('std2.sqlite')
    # step2 : define cursor
    cur = conn.cursor()
    # step3: execute SQL statement
    # select <field name(s)> from table
    # select std_id, dept from std_info
    cur.execute('''select * from std_info where std_id={}'''.format(student_id))
    # step4: fetch records
    rows = cur.fetchall()
    # print(rows)

    return render_template('std08.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
