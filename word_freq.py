from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/word_count', methods=['GET', 'POST'])
def word_count():
    counts = {}
    most_freq = None
    if request.method == 'POST':
        text = request.form['mytext']
        if text:
            for word in text.split():
                counts[word] = counts.get(word, 0) + 1

            most_freq = sorted([(v, k) for k, v in counts.items()], reverse=True)[0]
    return render_template('word_count.html', counts=counts, most_freq=most_freq)


if __name__ == '__main__':
    app.run(debug=True)
