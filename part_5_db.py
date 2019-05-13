import sqlite3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    conn = sqlite3.connect('std.sqlite')
    cur = conn.cursor()
    cur.execute('''select * from students''')
    rows = cur.fetchall()
    print(rows)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
