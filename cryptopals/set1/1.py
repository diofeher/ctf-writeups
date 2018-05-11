import base64

def hex_to_b64(text):
    hx = text.decode('hex')
    return base64.b64encode(hx)

st = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# I'm killing your brain like a poisonous mushroom
assert hex_to_b64(st) == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
