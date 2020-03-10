# coding: utf-8
from flask import Flask, request, make_response, send_from_directory, send_file, render_template
from main import error
import time
import config


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app = Flask(__name__, static_url_path='/static')  # 初始化一个Flask对象

app.after_request(after_request)  # 跨域支持


# 静态资源返回
@app.route('/<path:path>')
def send_assets(path):
    return send_from_directory(app.root_path, path)


@app.errorhandler(404)
def miss404(e):
    resp = make_response(error.ret_404(), 404)
    resp.headers["Content-Type"] = "application/json; charset=UTF-8"
    resp.headers["Date"] = time.time()
    return resp


@app.errorhandler(500)
def miss500(e):
    resp = make_response(error.ret_500(), 500)
    resp.headers["Content-Type"] = "application/json; charset=UTF-8"
    resp.headers["Date"] = time.time()
    return resp


@app.route('/test')
def test():
    ret_test = 'If you can see this line of text, the service started successfully'
    resp = make_response(ret_test, 200)
    resp.headers["Content-Type"] = "application/json; charset=UTF-8"
    resp.headers["Date"] = time.time()
    return resp


@app.route('/barrageDisplay')
def barrageDisplay():
    return app.send_static_file('index.html')


# 以下为API部分
# Data: 2020-03-10

@app.route('/barrage_bd')
def barrageDisplay():
    return app.send_static_file('index.html')












if __name__ == '__main__':
    app.run(config.host, port=config.port)
