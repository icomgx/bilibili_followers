# coding: utf-8

from main.controller import app
import config


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)