from flask import Flask, render_template
import requests
from post import Post

post_objects = []
blogs = requests.get("https://api.npoint.io/3259efdfcb16544ffd13").json()
count = 0
for blog in blogs:
    post_obj = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    post_obj.uniqueId = count
    post_objects.append(post_obj)
    count += 1


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", blogs=post_objects)


@app.route("/blogs/<uniqueId>")
def blog(uniqueId):
    return render_template("blog.html", blog=post_objects[int(uniqueId)])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3020, debug=True)
