from datetime import datetime

from flask import Flask, render_template

import requests

app = Flask(__name__)

year = datetime.now().year


@app.route("/")
def home():
    return render_template("index.html", year=year)


# print()


@app.route("/guess/<name>")
def guess(name):
    gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    return render_template("guess.html", name=name.capitalize(), gender=gender.capitalize(), age=age)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
