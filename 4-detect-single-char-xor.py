#!/usr/bin/env python3

from matasano01 import xor_with_key, rate_text, bruteforce_single_xor

if __name__ == '__main__':
    file = open('inputs/4.txt', 'r', encoding='utf-8')
    lines = file.read().splitlines()

    # build array of every line's lowest badness
    decoded_list = []
    for l in lines:
        l_key = ord(bruteforce_single_xor(l))
        decoded_list.append(xor_with_key(l, l_key))

    # find the line with the lowest badness in the set
    badness_list = []
    for d in decoded_list:
        d_badness = rate_text(d)
        badness_list.append(d_badness)

    # get index of lowest badness
    min_i = badness_list.index(min(badness_list))

    print(decoded_list[min_i].decode('utf-8'), end='')

