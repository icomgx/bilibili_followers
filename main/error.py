# coding: utf-8
import json


def ret_404():
    res_404 = {"code": "404", "message": "没有找到该方法，请检查是否错误。"}
    return json.dumps(res_404)


def ret_500():
    res_500 = {"code": "500", "message": "系统错误。"}
    return json.dumps(res_500)


