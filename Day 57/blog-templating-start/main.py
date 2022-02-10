from flask import Flask, render_template
from post import Post

app = Flask(__name__)
posts = Post()


@app.route('/')
def home():
    return render_template("index.html", blogs=posts.get_posts())


@app.route("/post/<num>")
def post(num):
    post_data = posts.get_post(int(num))
    return render_template("post.html", post_data=post_data)


if __name__ == "__main__":
    app.run(debug=True)
