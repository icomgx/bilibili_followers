# coding: utf-8
import os
import base64


def create_keys():
    secret_key = os.urandom(16)
    return str(secret_key)


if __name__ == '__main__':
    key = create_keys()
    print(key)
