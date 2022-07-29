#!/usr/bin/env python3

from matasano import repeating_key_xor

if __name__ == '__main__':
    test_str = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    result_str = b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'.upper()

    encoded = repeating_key_xor(test_str, 'ICE')

    if (encoded == result_str):
        print('Success!')
    else:
        print('Failure')

