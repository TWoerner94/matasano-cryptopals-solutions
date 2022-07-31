#!/usr/bin/env python3

from matasano1 import decode_hex, fixed_xor

if __name__ == '__main__':
    test_str1 = decode_hex('1c0111001f010100061a024b53535009181c')
    test_str2 = decode_hex('686974207468652062756c6c277320657965')
    test_expected = decode_hex('746865206b696420646f6e277420706c6179')

    if (fixed_xor(test_str1, test_str2) == test_expected):
        print('Success!')
    else:
        print('Failure')
