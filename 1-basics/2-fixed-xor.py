#!/usr/bin/env python3

import base64

def fixed_xor(str1, str2):
    str1_raw = base64.b16decode(str1, casefold=True)
    str2_raw = base64.b16decode(str2, casefold=True)
    xor_result = (bytes(x ^ y for (x, y) in zip (str1_raw, str2_raw)))
    return xor_result.hex()

if __name__ == '__main__':
    test_str1 = '1c0111001f010100061a024b53535009181c'
    test_str2 = '686974207468652062756c6c277320657965'
    test_expected = '746865206b696420646f6e277420706c6179'

    if (fixed_xor(test_str1, test_str2) == test_expected):
        print('Success!')
    else:
        print('Failure')
