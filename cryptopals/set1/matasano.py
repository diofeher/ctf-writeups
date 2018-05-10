import base64

def hex_to_b64(text):
    hx = text.decode('hex')
    return base64.b64encode(hx)


def xor_strings(text1, text2):
    lst = [chr(ord(a) ^ ord(b)) for a, b in zip(text1.decode('hex'), text2.decode('hex'))]
    print ''.join(lst)
    return ''.join(lst).encode('hex')