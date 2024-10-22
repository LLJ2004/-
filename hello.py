from datetime import datetime
from flask import Flask, redirect, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html') as fh:
        return fh.read()

@app.route('/upload', methods=["POST"])
def upload():
    # 获取文件流
    obj = request.files.get('filename')
    # 获取文件名称
    # file_name = secure_filename(obj.filename)
    file_name = obj.filename
    print("获取上传文件的名称为[%s]" % file_name)
    tmp = "copy data\\{} test_01.mp4".format(file_name)
    os.system(tmp)
    os.system("Main.exe")
    return redirect(request.referrer)