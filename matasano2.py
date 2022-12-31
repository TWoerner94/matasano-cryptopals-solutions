from Crypto.Cipher import AES
from random import randbytes, randrange, random
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

'''11 encrypt with random key'''
def encrypt_with_randkey(plaintext, keylength):
    random_key = randbytes(keylength)
    padding_before = randbytes(randrange(5, 11))
    padding_after = randbytes(randrange(5, 11))
    is_ecb = round(random())

    full_plaintext = padding_before + plaintext + padding_after
    padding_needed = keylength - (len(full_plaintext) % keylength)

    padded_plaintext = pkcs7_pad(full_plaintext, len(full_plaintext) + padding_needed)

    if is_ecb:
        cipher = AES.new(random_key, AES.MODE_ECB)
    else:
        iv = randbytes(keylength)
        cipher = AES.new(random_key, AES.MODE_CBC, iv=iv)

    return cipher.encrypt(padded_plaintext)

'''11 returns true if ecb mode is used, false for cbc'''
def encryption_oracle(ciphertext):
    BLOCK_LENGTH = 16
    
    # check if second and third blocks are the same
    block_2 = ciphertext[BLOCK_LENGTH:BLOCK_LENGTH * 2]
    block_3 = ciphertext[BLOCK_LENGTH * 2:BLOCK_LENGTH * 3]
    
    return block_2 == block_3



