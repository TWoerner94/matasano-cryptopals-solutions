from Crypto.Cipher import AES
from matasano1 import fixed_xor

'''9 pads the input byte array up to target_length'''
def pkcs7_pad(topad, target_length):
    result = bytearray(topad)
    length_difference = target_length - len(topad)
    for i in range(length_difference):
        result.append(length_difference)

    return result

'''10 encrypt plaintext using aes in cbc mode'''
def aes_cbc_encrypt(plaintext, key, iv):
    KEYSIZE = 16

    cipher = AES.new(key, AES.MODE_ECB)

    n_blocks = int(len(plaintext) / KEYSIZE)

    # SPLIT up the data into blocks with length = KEYSIZE
    blocks_in_data = []
    for i in range(n_blocks):
        lower_bound = KEYSIZE * i
        upper_bound = lower_bound + KEYSIZE
        block = plaintext[lower_bound:upper_bound]

        blocks_in_data.append(block)

    # loop through blocks and encrypt them using CBC, storing the previous ciphertext
    b_previous = iv
    result = bytearray(b'')
    for b in blocks_in_data:
        xored = fixed_xor(b_previous, b)
        xored_encrypted = cipher.decrypt(xored)
        result += xored_encrypted
        b_previous = xored_encrypted
    return bytes(result)

'''10 decrypt ciphertext using aes in cbc mode'''
def aes_cbc_decrypt(plaintext, key, iv):
    KEYSIZE = 16

    cipher = AES.new(key, AES.MODE_ECB)

    n_blocks = int(len(plaintext) / KEYSIZE)

    # split up the data into blocks with length = KEYSIZE
    blocks_in_data = []
    for i in range(n_blocks):
        lower_bound = KEYSIZE * i
        upper_bound = lower_bound + KEYSIZE
        block = plaintext[lower_bound:upper_bound]

        blocks_in_data.append(block)

    # loop through blocks and decrypt them using CBC, storing the previous plaintext
    result = bytearray(b'')
    b_previous = iv
    for b in blocks_in_data:
        b_decrypted = cipher.decrypt(b)
        xored = fixed_xor(b_previous, b_decrypted)
        result += xored
        b_previous = b
    return bytes(result)
