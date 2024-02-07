from flask import Flask, render_template
from datetime import datetime
from random import randint
import requests


app = Flask(__name__)

@app.route('/')
def home():
    template_name = 'index.html'
    random_number = randint(1, 10)
    current_year = datetime.now().year
    return render_template(template_name, num=random_number, year=current_year)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
