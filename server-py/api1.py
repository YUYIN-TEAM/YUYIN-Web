import os
import time
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import make_response
import json
import main
import making
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route('/rec', methods=['GET', 'POST'])
def rec():
    name = request.args.get('name')
    style = request.args.get('style')
    # cmd = "python main.py " + name + " " + style
    try:
        rec = main.main_rec(name, style)
        result = {
            'status': 'OK',
            'responseText': rec
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response
    except:
        result = {
          'status': 'ERROR',
          'responseText': '0'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response

@app.route('/make', methods=['GET', 'POST'])
def make():
    music_name = request.args.get('music_name')
    style = request.args.get('style')
    # cmd = "python main.py " + name + " " + style
    try:
        making.main_make(music_name, style)
        result = {
            'status': 'OK',
            # 'responseText': 'done'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response
    except:
        result = {
            'status': 'ERROR',
            # 'responseText': 'done'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response

@app.route('/make_pg', methods=['GET', 'POST'])
def make_pg():
    # name = request.args.get('name')
    # style = request.args.get('style')
    f = open("./list/process.txt")
    try:
        a = f.read()
        f.close()
        result = {
            'status': "OK",
            'responseText': a
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response
    except:
        f.close()
        result = {
          'status': '404',
          'responseText': 'Error'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response

@app.route('/rec_pg', methods=['GET', 'POST'])
def rec_pg():
    # name = request.args.get('name')
    # style = request.args.get('style')
    f = open("./list/rec_process.txt")
    try:
        a = f.read()
        f.close()
        result = {
            'status': "OK",
            'responseText': a
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response
    except:
        f.close()
        result = {
            'status': '404',
            'responseText': 'Error'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response

@app.route('/rec_res', methods=['GET', 'POST'])
def rec_res():
    # name = request.args.get('name')
    # style = request.args.get('style')
    f = open("./rec_result.txt")
    try:
        a = f.read()
        f.close()
        result = {
            'status': "OK",
            'responseText': a
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response
    except:
        f.close()
        result = {
            'status': '404',
            'responseText': 'Error'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response
if __name__ == '__main__':
    # happy begin
    app.run(host='localhost', port=9001, debug=app.config['DEBUG'])
    app.run(host='0.0.0.0', port=9001, debug=app.config['DEBUG'])
    # happy end