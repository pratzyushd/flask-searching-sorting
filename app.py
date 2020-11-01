from time import time
from flask import Flask, render_template, request
from sortingPY import bubble
from sortingPY import merge
from searchingPY import linear
from searchingPY import binary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bubblesort")
def displayBubble():
    return render_template("sorting/bubble.html")

@app.route('/bubblesort', methods=['POST'])
def bubbleSort():
    inputList = request.form.getlist("text")[0]
    numbers = [int(x) for x in inputList.split(",")]
    start = time()
    sortedList = bubble.bubbleSort(numbers)
    timeTaken = time() - start
    return render_template("sorting/bubble.html", processed=sortedList, time=timeTaken)


@app.route("/mergesort")
def displayMerge():
    return render_template("sorting/merge.html")

@app.route('/mergesort', methods=['POST'])
def mergeSort():
    inputList = request.form.getlist("text")[0]
    numbers = [int(x) for x in inputList.split(",")]
    start = time()
    sortedList = merge.mergeSort(numbers)
    timeTaken = time() - start
    return render_template("sorting/merge.html", processed=sortedList, time=timeTaken)
