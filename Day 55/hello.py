from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def bold():
        return f'<b>{func()}</b>'

    return bold


def make_emphasis(func):
    def emphasis():
        return f'<em>{func()}</em>'

    return emphasis


def make_underlined(func):
    def underlined():
        return f'<u>{func()}</u>'

    return underlined


@app.route("/")
def home():
    return "<h1 style='text-align: center'>Welcome</h1>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "BYE!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
