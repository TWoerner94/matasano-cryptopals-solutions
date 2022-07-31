#!/usr/bin/env python3

import base64
import math
from matasano01 import encode_hex, decode_hex, get_hamming, repeating_key_xor, bruteforce_single_xor, rate_text

if __name__ == '__main__':
    file = open('inputs/6.txt', 'r')
    data_b64 = file.read()

    # decode from base64
    data = base64.b64decode(data_b64)

    # bruteforce keysizes
    hamming_list = []
    for ks in range(2,40):
        str1 = data[:ks]
        str2 = data[ks:ks * 2]
        str3 = data[ks * 2:ks * 3]
        str4 = data[ks * 3:ks * 4]

        hamming1 = get_hamming(str1, str2) / ks
        hamming2 = get_hamming(str2, str3) / ks
        hamming3 = get_hamming(str3, str4) / ks

        avg_hamming = (hamming1 + hamming2 + hamming3) / 3
        hamming_list.append({'keysize': ks, 'hamming': avg_hamming})

    hamming_list_sorted = sorted(hamming_list, key=lambda d: d['hamming'])
    hamming_top = hamming_list_sorted[:3]

    possible_keys = []
    for h in hamming_top:
        keysize = h['keysize']
        
        # break ciphertext into blocks with length = keysize
        data_blocks = []
        for i in range(math.ceil(len(data) / keysize)):
            lower_bound = keysize * i
            upper_bound = lower_bound + keysize
            data_blocks.append(data[lower_bound:upper_bound])

        # build the transposed blocks
        transposed_blocks = []
        for i in range(keysize):
            transposed_b = bytearray(b'')
            for b in data_blocks:
                if i < len(b):
                    transposed_b.append(b[i])
            transposed_blocks.append(transposed_b)

        # single-character xor each transposed block
        key = ''
        for t in transposed_blocks:
            t_hex = encode_hex(t)
            key_char = bruteforce_single_xor(t_hex)
            key += key_char
        possible_keys.append(key)

    # compare badnesses for the different keys
    badness_for_keys = []
    for k in possible_keys:
        decrypted = decode_hex(repeating_key_xor(data, k))
        badness = rate_text(decrypted)
        badness_for_keys.append({'key': k, 'badness': badness, 'plaintext': decrypted})

    # pick the key with the lowest badness
    min_badness = min(badness_for_keys, key=lambda d: d['badness'])

    # decrypt the text
    print(min_badness['plaintext'].decode('utf-8'))

