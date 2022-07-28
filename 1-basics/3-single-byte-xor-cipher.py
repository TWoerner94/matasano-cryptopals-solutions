#!/usr/bin/env python3

import base64

def decode(hex_string):
    return base64.b16decode(hex_string, casefold=True)

def xor_with_key(test_data, key):
    data_raw = decode(test_data)
    return bytes(x ^ key for x in data_raw)

'''i am using the frequency of non-alphabetic characters here, since the
dataset is too small for character frequency analysis'''
def rate_text(text):
    common_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    counter = 0
    for i in text:
        if not chr(i) in common_chars:
            counter += 1
    return counter

def run(test_string):
    counter_list = []
    for i in range(0,255):
        counter_list.append(rate_text(xor_with_key(test_string, i)))
    minimum_index = counter_list.index(min(counter_list))
    print('Likeliest solution: %s' % chr(minimum_index))
    print('Decoded text: %s' % xor_with_key(test_string, minimum_index).decode('utf-8'))

if __name__ == '__main__':
    test = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    run(test)
