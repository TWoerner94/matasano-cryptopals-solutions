import base64

'''decoding hexadecimal strings to raw bytes'''
def decode_hex(hex_string):
    return base64.b16decode(hex_string, casefold=True)

'''converting hexadecimal bytes to base64'''
def hex_to_b64(data_hex):
    data_raw = decode_hex(data_hex)
    data_b64 = base64.b64encode(data_raw)
    return data_b64

'''xor'ing two strings of the same length'''
def fixed_xor(str1, str2):
    str1_raw = decode_hex(str1)
    str2_raw = decode_hex(str2)
    xor_result = (bytes(x ^ y for (x, y) in zip(str1_raw, str2_raw)))
    return xor_result.hex()

'''xor'ing a string with a single character'''
def xor_with_key(test_data, key):
    data_raw = decode_hex(test_data)
    return bytes(x ^ key for x in data_raw)

'''rating a piece of text to determine if it is english language plaintext,
using the frequency of non-alphabetic characters since the dataset will
generally be too small for character frequency analysis'''
def rate_text(text):
    common_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '!?.,"
    counter = 0
    for i in text:
        if not chr(i) in common_chars:
            counter += 1
    return counter

'''find out what character a string was xor'ed with'''
def bruteforce_single_xor(test_string):
    badness_list = []
    for i in range(0,255):
        badness = rate_text(xor_with_key(test_string, i))
        badness_list.append(badness)
    
    # get the index of the lowest badness result within the list
    minimum_index = badness_list.index(min(badness_list))

    # return char that was used for encoding
    return chr(minimum_index)



