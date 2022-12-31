#!/usr/bin/env python3

from matasano2 import encrypt_with_randkey, encryption_oracle

if __name__ == '__main__':
    '''
    length of this variable has to be at least twice the block length plus twice
    the max padding to ensure that the ciphertext will contain a repeating block
    if ecb is used
    '''
    to_encrypt = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    encrypted_data = encrypt_with_randkey(to_encrypt, 16)
    
    print(encryption_oracle(encrypted_data))
