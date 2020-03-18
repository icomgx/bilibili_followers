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


# 404错误返回
@app.errorhandler(404)
def miss404(e):
    resp = make_response(error.ret_404(), 404)
    resp.headers["Content-Type"] = "application/json; charset=UTF-8"
    resp.headers["Date"] = time.time()
    return resp


# 500错误返回
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
# Modify Data: 2020-03-18

# ------弹幕类接口------
# Modify Data: 2020-03-18
# 大屏用弹幕接口
@app.route('/api/barrage/display')
def barrageApiDisplay():
    pass


# 标准弹幕接口
@app.route('/api/barrage/std')
def barrageApiStd():
    pass


# 标准设备弹幕接口
@app.route('/api/barrage/device')
def barrageApiDevice():
    pass


# ------粉丝类接口------
# Modify Data: 2020-03-18
# 标准粉丝数接口
@app.route('/api/followers/count')
def followersCount():
    pass


# 标准设备粉丝数接口
@app.route('/api/followers/device')
def followersDevice():
    pass


# 保留自定义接口
@app.route('/api/followers/customize')
def followersCustomize():
    pass


# ------系统相关类接口------
# Modify Data: 2020-03-18
# 生成开发者密钥
@app.route('/api/system/developerkey/create')
def createDeveloperKey():
    pass


# 停用开发者密钥
@app.route('/api/system/developerkey/disable')
def disableDeveloperKey():
    pass


# 注销开发者密钥
@app.route('/api/system/developerkey/delete')
def deleteDeveloperKey():
    pass

# ------设备功能相关接口------
# Modify Data: 2020-03-18
# 生成设备码
@app.route('/api/device/dcode/create')
def dcodeCreate():
    pass


# 停用设备码
@app.route('/api/device/dcode/disable')
def dcodeDisable():
    pass


# 注销设备码
@app.route('/api/device/dcode/delete')
def dcodeDelete():
    pass


# ------统一查询接口------
# Modify Data: 2020-03-18
# 查询所有开发者密钥及状态
@app.route('/api/query/developerkey/status')
def queryDeveloperketStatus():
    pass


# 查询所有设备码及状态
@app.route('/api/query/dcode/status')
def querydcodeStatus():
    pass






# ------其他功能相关接口------
# Modify Data: 2020-03-18
# 图片转换bitmap
@app.route('/api/tools/other/imageToBitmap')
def imageToBitmap():
    pass


