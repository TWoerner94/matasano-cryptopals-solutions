'''9 pads the input byte array up to target_length'''
def pkcs7_pad(topad, target_length):
    result = bytearray(topad)
    length_difference = target_length - len(topad)
    for i in range(length_difference):
        result.append(length_difference)

    return result
