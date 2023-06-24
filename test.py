import random
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

db = {
        'Russia': 'Moscow',
        'USA': 'Washington',
        'Japan': 'Tokyo',
        'Italy': 'Rome',
        'Spain': 'Madrid',
        'Portugal': 'Lisbon',
        'France': 'Paris',
        'Germany': 'Berlin',
        'UK': 'London',
        'China': 'Beijing'
    }
country = random.choice(list(db))
correct_answer = 0


@app.route('/')
def index():
    return render_template('form.html', country=country, correct=correct_answer)


@app.route('/', methods=['POST'])
def result():
    res = str
    country = request.form.get("country", type=str)
    capital = request.form.get("capital", type=str)
    correct_answer = request.form.get("correct", type=int)
    for key in db:
        if key == country:
            if db[key] == capital:
                res = 'Correct'
                correct_answer += 1
            else:
                res = 'Incorrect'
    if res == 'Correct':
        country = random.choice(list(db))
    capital = ""
    return render_template('form.html', country=country, capital=capital, result=res, correct=correct_answer)


if __name__ == '__main__':
    app.run()
