from flask import Flask
from flask import jsonify
from flask_restful import Api


app = Flask(__name__)

@app.route('/')
def post():
    """
    """
    return jsonify({})
