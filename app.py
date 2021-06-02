from flask import Flask, jsonify, request
from quote import getRandom

app = Flask(__name__)

@app.route("/")
def homepage():
    return '<p>use <b>/random</b> at the end to get quotes..."</p>'


@app.route("/random")
def quotes():
    if request.method == 'GET':
        return jsonify(getRandom())
    
if __name__ == '__main__':
    app.run()