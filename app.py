
from flask import Flask, jsonify, request
from Summarize import summarize

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def get_summarize():
    """
    Summarize this bitch
    """
    data = request.form['text']
    return jsonify({'result': summarize(str(data))})


if __name__ == '__main__':
    app.run()
