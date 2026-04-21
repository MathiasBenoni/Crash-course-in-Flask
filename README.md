# Flask crash-course

This is a crash-course of python – Flask

If something failes, write this line in your terminal

```
lsof -i :5000
```

## Install dependencies

### Install Flask

```
pip install flask
```

## Make folder stucture

```text
project_root/
│
├── app.py
│
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
│
└── templates/
    └── index.html
```

---

### Make basic stucture

```py
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "<p> Hello world! </p>"

if __name__ == "__main__":
    app.run(debug=True)
```

### Introduce routes

```py
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "<p> Hello world! </p>"

@app.route("/test")
def test():
    return "Test"

if __name__ == "__main__":
    app.run(debug=True)
```

### Introduce html files

```py
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index")


if __name__ == "__main__":
    app.run(debug=True)
```

### Introduce form-submission

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Flask crash-course</title>
  </head>
  <body>
    <form method="POST" action="/login">
      <label for="username"> Username </label>
      <input type="text" id="username" />
      <button type="submit">Login</button>
    </form>
  </body>
</html>
```

```py
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
```
