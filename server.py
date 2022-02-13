from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

booknum = 0
transactions = []
bookshelf = []


@app.route('/bookshelf/getBookshelf', methods=['GET'])
def getBookshelf():
    return jsonify(bookshelf)


@app.route('/bookshelf/getHistory', methods=['GET'])
def getHistory():
    return jsonify(transactions)


@app.route('/bookshelf/getBookNum', methods=['GET'])
def getBookNum():
    return jsonify({"book num": booknum})


@app.route('/bookshelf/add', methods=['POST'])
def addBook():
    global booknum
    booknum += 1
    book = request.get_json()
    bookshelf.append({"title": book["title"],
                      "author": book["author"]})

    transaction = request.get_json()
    transaction["type"] = "add"
    transaction["time"] = datetime.now()
    transactions.append(transaction)
    return jsonify({"num books": booknum})


@app.route('/bookshelf/remove', methods=['POST'])
def removeBook():
    global booknum, bookshelf
    transaction = request.get_json()
    transaction["type"] = "remove"
    transaction["time"] = datetime.now()
    transactions.append(transaction)
    if booknum > 0:
        for i in range(booknum):
            if bookshelf[i]["title"] == transaction["title"]:
                bookshelf.pop(i)
                booknum -= 1
                return jsonify({"num books": booknum})
    return jsonify({"num books": booknum})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
