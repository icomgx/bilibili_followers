# coding: utf-8

from io import open
from json import load as load_json_file

f = open("config.json", "r")
cfg = load_json_file(f)
f.close()

host = "127.0.0.1"
port = int(cfg['port'])
uid = str(cfg['uid'])
