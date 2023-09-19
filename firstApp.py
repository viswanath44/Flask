# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, jsonify

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# # which tells the application which URL should call
# # the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return ('Hello World!!!')

@app.route('/home')
def display_home():
	return ('home content!')

@app.route('/add', methods =['POST'])
def addNumbers():
	numbers = request.json
	print(numbers)
	a = int(numbers.get('a'))
	b = int(numbers.get('b'))
	c = a + b
	return jsonify({'result' : c})

@app.route('/json_example', methods=['POST'])
def handle_json():
    data = request.json
    print(data.get('name'))
    print(data.get('age'))
    return data















#
# @app.route('/yourName'))
# # ‘/’ URL is bound with hello_world() function.
# def displayName(name):
# 	return 'Hello World'
#
# @app.route('/add')
# # ‘/’ URL is bound with hello_world() function.
# def add_numbers():
# 	return 2

# @app.route('/echo', methods=['POST'])
# def hello():
#    return jsonify(request.json)

# @app.route('/jsonInput/<input>', methods=['GET', 'POST'])
# def add_message(input):
#     content = request.json
#     print(content['mytext'])
#     return jsonify({"uuid":input})

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
