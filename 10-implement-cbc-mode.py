#!/usr/bin/env python3

import base64

from Crypto.Cipher import AES
from matasano1 import fixed_xor
from matasano2 import aes_cbc_decrypt

if __name__ == '__main__':
    KEYSIZE = 16

    file = open('inputs/10.txt', 'rb')
    data = base64.b64decode(file.read())

    key = b'YELLOW SUBMARINE'
    iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    decrypted = aes_cbc_decrypt(data, key, iv)
    print(decrypted.decode('utf-8'))

