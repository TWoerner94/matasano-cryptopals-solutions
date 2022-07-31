#!/usr/bin/env python3

from matasano1 import hex_to_b64

if __name__ == '__main__':
    test_hex = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    test_b64 = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    encoded = hex_to_b64(test_hex)

    if (encoded == test_b64):
        print('Success!')
    else:
        print('Failure')
