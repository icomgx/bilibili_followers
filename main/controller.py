import time

from flask import Flask, request, make_response, send_from_directory, send_file, render_template
from flask_restful import reqparse, abort, Api, Resource
from main import error, b2rrage, fo2owers, k2ey, d2evice


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app = Flask(__name__, static_url_path='/static')  # 初始化一个Flask对象
api = Api(app)

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


# 保留测试接口
@app.route('/test')
def test():
    ret_test = 'If you can see this line of text, the service started successfully'
    resp = make_response(ret_test, 200)
    resp.headers["Content-Type"] = "application/json; charset=UTF-8"
    resp.headers["Date"] = time.time()
    return resp


# 粉丝弹幕大屏
@app.route('/barrageDisplay')
def barrageDisplay():
    return app.send_static_file('index.html')


# 以下为API部分
# Modify Data: 2020-03-19

# ------弹幕类接口------
# Modify Data: 2020-03-19
class Barrage(Resource):
    def get(self, action_name):
        if action_name == 'display':
            ra = b2rrage.display()
            return ra
        elif action_name == 'standard':
            ra = b2rrage.standard()
            return ra
        elif action_name == 'device':
            ra = b2rrage.device()
            return ra


# ------粉丝类接口------
# Modify Data: 2020-03-19
class Followers(Resource):
    def get(self, action_name):
        if action_name == 'count':
            ra = fo2owers.count()
            return ra
        elif action_name == 'device':
            ra = fo2owers.device()
            return ra
        elif action_name == 'customize':
            ra = fo2owers.customize()
            return ra


# ------系统相关类接口------
# Modify Data: 2020-03-19
class Developerkey(Resource):
    def get(self, action_name):
        if action_name == 'create':
            ra = k2ey.create()
            return ra
        elif action_name == 'disable':
            ra = k2ey.disable()
            return ra
        elif action_name == 'delete':
            ra = k2ey.delete()
            return ra
        elif action_name == 'status':
            ra = k2ey.status()
            return ra


# ------设备功能相关接口------
# Modify Data: 2020-03-19
class Device(Resource):
    def get(self, action_name):
        if action_name == 'create':
            ra = d2evice.create()
            return ra
        elif action_name == 'disable':
            ra = d2evice.disable()
            return ra
        elif action_name == 'delete':
            ra = d2evice.delete()
            return ra
        elif action_name == 'status':
            ra = d2evice.status()
            return ra


# ------其他功能相关接口------
# Modify Data: 2020-03-19
class Other(Resource):
    def get(self, acticon_name):
        if acticon_name == 'imageToBitmap':
            return 'imageToBitmap'


# 设置路由
api.add_resource(Barrage, '/api/barrage/<action_name>')
api.add_resource(Followers, '/api/followers/<action_name>')
api.add_resource(Developerkey, '/api/developerkey/<action_name>')
api.add_resource(Device, '/api/device/<action_name>')
api.add_resource(Other, '/api/other/<action_name>')


if __name__ == '__main__':
    app.run()
