# utils.py
def xor(b1, b2):
    """ XOR two byte sequences """
    return bytes(x ^ y for x, y in zip(b1, b2))