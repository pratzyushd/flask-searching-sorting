from datetime import datetime
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/hello")
@app.route("/hello/<name>")
def helloThere(name = None):
    return render_template("hello_there.html", name = name, date = datetime.now())