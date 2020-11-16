from datetime import datetime
# import csv
from flask import Flask, render_template, request
from sortingPY import bubble
from sortingPY import merge
from searchingPY import linear
from searchingPY import binary

UPLOAD_FOLDER = "/uploads"
ALLOWED_FILES = {"csv"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bubblesort")
def displayBubble():
    return render_template("sorting/bubble.html")

@app.route('/bubblesort', methods=['POST'])
def bubbleSort():
    inputList = request.form.getlist("numbers")[0]
    numbers = [int(x) for x in inputList.split(",") if x != " " and x.isdigit()]
    start = datetime.now()
    sortedList = bubble.bubbleSort(numbers)
    timeDiff = datetime.now() - start
    timeTaken = timeDiff.total_seconds() * 1000
    return render_template("sorting/bubble.html", processed=sortedList, time=timeTaken)



@app.route("/mergesort")
def displayMerge():
    return render_template("sorting/merge.html")

@app.route('/mergesort', methods=['POST'])
def mergeSort():
    inputList = request.form.getlist("numbers")[0]
    numbers = [int(x) for x in inputList.split(",") if x != " " and x.isdigit()]
    start = datetime.now()
    sortedList = merge.mergeSort(numbers)
    timeDiff = datetime.now() - start
    timeTaken = timeDiff.total_seconds() * 1000
    return render_template("sorting/merge.html", processed=sortedList, time=timeTaken)

@app.route("/linearsearch")
def displayLinear():
    return render_template("searching/linear.html")

@app.route('/linearsearch', methods=['POST'])
def linearSearch():
    inputList = request.form.getlist("numbers")[0]
    toFind = int(request.form.getlist("find")[0])
    numbers = [int(x) for x in inputList.split(",") if x != " " and x.isdigit()]
    start = datetime.now()
    found = linear.linearSearch(numbers, toFind)
    timeDiff = datetime.now() - start
    timeTaken = timeDiff.total_seconds() * 1000
    return render_template("searching/linear.html", found=found, time=timeTaken)


@app.route("/binarysearch")
def displayBinary():
    return render_template("searching/binary.html")

@app.route('/binarysearch', methods=['POST'])
def binarySearch():
    inputList = request.form.getlist("numbers")[0]
    toFind = int(request.form.getlist("find")[0])
    numbers = [int(x) for x in inputList.split(",") if x != " " and x.isdigit()]
    start = datetime.now()
    found = binary.binarySearch(numbers, toFind)
    timeDiff = datetime.now() - start
    timeTaken = timeDiff.total_seconds() * 1000
    return render_template("searching/binary.html", found=found, time=timeTaken)
