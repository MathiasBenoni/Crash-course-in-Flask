from flask import *

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    return "Nice"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
