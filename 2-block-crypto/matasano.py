'''pads the input byte array up to target_length using \x04 bytes'''
def pkcs7_pad(topad, target_length):
    result = topad
    length_difference = target_length - len(topad)
    for i in range(length_difference):
        result += b'\x04'
    return result
