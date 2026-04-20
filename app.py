from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "<p> Hello world! </p>"



if __name__ == "__main__":
    app.run(debug=True)