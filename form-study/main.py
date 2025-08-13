from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        result = ''
        return render_template('index.html', result=result)
    else:
        value = randint(1, 10)
        guess = int(request.form.get("number"))
        if guess == value:
            result = 'You won!'
            return render_template('index.html', result = result)
        else: 
            result = 'You lose!'
            correct_value = f'The correct number is {value}'
            return render_template('index.html', result = result, value = correct_value)
