from flask import (Flask, render_template)
import time
app = Flask(__name__)


@app.route("/hello")
def welcome():
    time.sleep(5)
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
