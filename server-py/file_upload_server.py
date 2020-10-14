# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
from flask import make_response
import os
import shutil
from pprint import pprint, pformat

app = Flask(__name__)
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    return response

@app.route('/upload', methods=['POST'])
def upload():
    destination_root_dir = "/etc/nginx/YUYIN/YUYIN1004/data/input_video"
    temp_root_dir = "/root/happy/docker_nginx/upload_dir"
    if request.method == 'POST':
        file_info = {
            "upload_file_name": request.values["file.name"],
            "upload_content_type":request.values["file.content_type"],
            "upload_tmp_path":request.values["file.path"].replace("/tmp/nginx_upload", "/root/happy/docker_nginx/upload_dir"),
            "upload_file_md5":request.values["file.md5"],
            "upload_file_size":request.values['file.size'],
            "upload_project_name":request.args["upload_project_name"]
        }
        pprint(file_info)

        file_temp_path = file_info["upload_tmp_path"]
        file_destination_path = os.path.join(destination_root_dir, file_info["upload_project_name"],file_info["upload_file_name"])
        os.makedirs(os.path.join(destination_root_dir, file_info["upload_project_name"]), exist_ok=True)

        shutil.move(file_temp_path, file_destination_path)

    # return render_template('docker_nginx/conf.d/index.html')
    #qjchen begin
    return add_header(make_response(jsonify(file_info)))
    #qjchen end
    #return ("upload success! \n %s"%(pformat(file_info))).replace("\n", "<br>")

@app.route('/mupload', methods=['POST'])
def mupload():
    destination_root_dir = "/etc/nginx/YUYIN/YUYIN1006/data/input_video"
    temp_root_dir = "/root/happy/docker_nginx/mupload_dir"
    if request.method == 'POST':
        file_info = {
            "upload_file_name": request.values["file.name"],
            "upload_content_type":request.values["file.content_type"],
            "upload_tmp_path":request.values["file.path"].replace("/tmp/nginx_mupload", "/root/happy/docker_nginx/mupload_dir"),
            "upload_file_md5":request.values["file.md5"],
            "upload_file_size":request.values['file.size'],
            "upload_project_name":request.args["upload_project_name"]
        }
        pprint(file_info)

        file_temp_path = file_info["upload_tmp_path"]
        file_destination_path = os.path.join(destination_root_dir, file_info["upload_project_name"],file_info["upload_file_name"])
        os.makedirs(os.path.join(destination_root_dir, file_info["upload_project_name"]), exist_ok=True)

        shutil.move(file_temp_path, file_destination_path)

    # return render_template('docker_nginx/conf.d/index.html')

    return ("upload success! \n %s"%(pformat(file_info))).replace("\n", "<br>")


if __name__ == '__main__':
    app.run(host='localhost', port=9004, debug=app.config['DEBUG'])
    #app.run(host='127.0.0.1', port=9090, debug=app.config['DEBUG'])