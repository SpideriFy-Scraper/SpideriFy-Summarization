
from flask import Flask, jsonify, request
from flask_cors import CORS
from summarize import summarize

app = Flask(__name__)
cors = CORS(app, resources={r"/predict/*": {"origins": "*"}})

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.TestingConfig')


@app.route('/predict', methods=['POST'])
def get_summarize():
    """
    Summarize this bitch
    """
    data = request.form['text']
    return jsonify({'result': summarize(str(data))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
