from flask import Flask
import random

guess_number = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1 style="text-align: center"> Guess a number between 0 and 9 </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style="margin: 0 auto">'


@app.route("/<int:num>")
def check(num):
    if num == guess_number:
        return '<h1 style="color: green">You Found Me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

    # high
    elif num > guess_number:
        return '<h1 style="color: violet">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    # low
    else:
        return '<h1 style="color: red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == '__main__':
    print(guess_number)
    app.run(debug=True, host="0.0.0.0", port=8080)
