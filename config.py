# coding: utf-8

from io import open
from json import load as load_json_file

f = open("config.json", "r")
cfg = load_json_file(f)
f.close()

host = str(cfg['host'])
port = int(cfg['port'])
uid = str(cfg['uid'])
