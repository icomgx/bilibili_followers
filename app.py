from flask import Flask, request, make_response
from main import error
import time
import config


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app = Flask(__name__, static_url_path='/static')  # 初始化一个Flask对象

app.after_request(after_request)  # 跨域支持


@app.errorhandler(404)
def miss(e):
    resp = make_response(error.ret_404(), 404)
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




if __name__ == '__main__':
    app.run(host=config.host, port=config.port)