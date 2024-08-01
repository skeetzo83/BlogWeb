from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_details():
    url = "https://api.npoint.io/2fee3334b405c694f8ba"
    response = requests.get(url=url)
    all_posts = response.json()
    return all_posts


def get_body(num):
    body = get_details()[num]["body"]
    title = get_details()[num]["title"]
    return render_template("post.html", title=title, body=body)


@app.route('/')
def home():
    title_names = [title["title"] for title in get_details()]
    subtitle_names = [subtitle["subtitle"] for subtitle in get_details()]
    return render_template("index.html", title_one=title_names[0], title_two=title_names[1], title_three=title_names[2],
                           subtitle_one=subtitle_names[0], subtitle_two=subtitle_names[1],
                           subtitle_three=subtitle_names[2])


@app.route('/blog/1')
def body_one():
    return get_body(0)


@app.route('/blog/2')
def body_two():
    return get_body(1)


@app.route('/blog/3')
def body_three():
    return get_body(2)


if __name__ == "__main__":
    app.run(debug=True)
