#!/usr/bin/env python3

import base64
from Crypto.Cipher import AES

if __name__ == '__main__':
    file = open('input_7.txt', 'r')
    data_b64 = file.read()
    data = base64.b64decode(data_b64)

    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(data).decode('utf-8')

    print(plaintext)
