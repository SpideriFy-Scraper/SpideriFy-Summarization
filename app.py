
from flask import Flask, jsonify, request
from Summarize import summarize

app = Flask(__name__)


@app.route('/predictions/summarization', methods=['POST'])
def post():
    """
    Summarize this bitch
    """

    data = request.form['text']

    return jsonify({'result': summarize(str(data))})
