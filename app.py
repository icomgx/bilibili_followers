from flask import Flask, request, make_response
import time


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app = Flask(__name__, static_url_path='/static')

app.after_request(after_request)