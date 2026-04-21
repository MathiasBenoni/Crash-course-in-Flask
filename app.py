from flask import *

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():

    username = request.form.get("username")
    if username == "admin":
        return "Nice"
    else:
        print(username)
        return "Not Nice"
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)
