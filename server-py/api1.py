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
CORS(app)


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
    except Exception as e:
        print(e)
        result = {
            'status': 'ERROR',
            'responseText': '0'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response


@app.route('/make', methods=['GET', 'POST'])
def make():
    name = str(request.args.get('name'))
    music_name = str(request.args.get('music_name'))
    style = str(request.args.get('style'))
    # cmd = "python main.py " + name + " " + style
    try:
        making.main_make(name, music_name, style)
        result = {
                'status':name+'.mp4 OK',
            # 'responseText': 'done'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response
    except Exception as e:
        print(e)
        result = {
            'status': 'ERROR',
            # 'responseText': 'done'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response


@app.route('/make_pg', methods=['GET', 'POST'])
def make_pg():
    name = request.args.get('name')
    # style = request.args.get('style')
    f = open("./list/"+name+"/process.txt")
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
    except Exception as e:
        print(e)
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
    name = request.args.get('name')
    # style = request.args.get('style')
    while True:
        try:
            f = open("./list/"+name+"/rec_process.txt")
            break
        except Exception as e:
            print(e)
            continue
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
    except Exception as e:
        print(e)
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
    name = request.args.get('name')
    # style = request.args.get('style')
    while True:
        try:
            f = open("/etc/nginx/YUYIN/YUYIN1004/list/"+name+"/rec_result.txt")
            break;
        except Exception as e:
            print(e)
            continue
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
    except Exception as e:
        print(e)
        f.close()
        result = {
            'status': '404',
            'responseText': 'Error'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response

@app.route('/del', methods=['GET', 'POST'])
def dele():
    name = request.args.get('name')
    vname = request.args.get('video_name')

    try:
        try:
            os.remove('/etc/nginx/YUYIN/YUYIN1004/data/input_video/'+name+'/'+vname)
        except:
            pass
        result = {
            'status': "OK",
            'responseText': name+'/'+vname+' is now deleted!'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response
    except Exception as e:
        print(e)
        result = {
            'status': '404',
            'responseText': 'Error'
        }
        response = make_response(jsonify(result))
        response = add_header(response)
        return response


if __name__ == '__main__':
    # happy begin
    # app.run(host='localhost', port=9001, debug=app.config['DEBUG'])
    app.run(host='0.0.0.0', port=9001, debug=app.config['DEBUG'])
    # happy end