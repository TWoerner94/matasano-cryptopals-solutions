from matasano import xor_with_key, bruteforce_single_xor

def run(test_string):
    minimum_index = bruteforce_single_xor(test_string)
    decoded_text = xor_with_key(test_string, ord(minimum_index)).decode('utf-8')
    print('Likeliest solution: %s' % minimum_index)
    print('Decoded text: %s' % decoded_text)

if __name__ == '__main__':
    test = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    run(test)

