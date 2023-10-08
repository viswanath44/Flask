from flask import Flask, request, jsonify
from first_app import addNumbers, handle_json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!!'


@app.route('/home')
def display_home():
    return 'home content!'


@app.route('/add', methods=['POST'])
def add():
    numbers = request.json
    result = addNumbers(numbers['num1'], numbers['num2'])
    return jsonify({'result': f'Sum of two numbers is {result}'})


@app.route('/authorise', methods=['POST'])
def authorise():
    data = request.json
    result = handle_json(data['name'], data['age'])
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
