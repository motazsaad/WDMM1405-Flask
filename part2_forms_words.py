from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/mostfreq', methods=['GET', 'POST'])
def mostfreq():
    result = None
    op = 'most frequent'
    if request.method == 'POST':
        text = request.form['mytext']
        if not text:
            result = 'please fil the form'
            # print(result)
        else:
            counts = {}
            for word in text.split():
                counts[word] = counts.get(word, 0) + 1
            result = sorted([(v, k) for k, v in counts.items()], reverse=True)[0]

    return render_template('words.html', op=op, result=result)


@app.route('/mostfreqtable', methods=['GET', 'POST'])
def mostfreqtable():
    counts = {}
    if request.method == 'POST':
        text = request.form['mytext']
        if not text:
            result = 'please fill the form'
            print(result)
        else:
            for word in text.split():
                counts[word] = counts.get(word, 0) + 1

    return render_template('words2.html', counts=counts)


if __name__ == '__main__':
    app.run(debug=True)
