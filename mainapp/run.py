from flask import (Flask, request, render_template)
import requests

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello():
    return "Running"


@app.route("/content")
def content():
    # Todo 1
    response = requests.get(url="http://XXXXX:3000/content")
    return render_template("content.html", response=response.text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
