#!/usr/bin/env python3

from matasano import decode_hex

if __name__ == '__main__':
    KEYSIZE = 16
    
    file = open('input_8.txt', 'r')
    lines = file.read().splitlines()

    for index, l in enumerate(lines):
        l_decoded = decode_hex(l)
        n_blocks = int(len(l_decoded) / KEYSIZE)

        # split up the line into blocks with length = KEYSIZE
        blocks_in_line = []
        for i in range(n_blocks):
            lower_bound = KEYSIZE * i
            upper_bound = lower_bound + KEYSIZE
            block = l_decoded[lower_bound:upper_bound]

            blocks_in_line.append(block)

        # check if any blocks are equal
        blocks_in_line_duplicates_removed = set(blocks_in_line)
        if not len(blocks_in_line) == len(blocks_in_line_duplicates_removed):
            print('The following line contains duplicate blocks: %s\n%s' % (index, l))
            print('This line is likely encrypted with AES in ECB mode.')

