#!/usr/bin/env python3

from matasano2 import pkcs7_pad

if __name__ == '__main__':
    test_str = b'YELLOW SUBMARINE'
    expected_result = b'YELLOW SUBMARINE\x04\x04\x04\x04'
    
    test_str_padded = pkcs7_pad(test_str, 20)

    if test_str_padded == expected_result:
        print('Success!')
    else:
        print('Failure')
