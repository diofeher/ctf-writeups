import base64
from Crypto.Cipher import AES

KEY = "YELLOW SUBMARINE"

cipher = AES.new(KEY, AES.MODE_ECB)

with open('7.txt') as f:
    text = base64.b64decode(f.read())

assert cipher.decrypt(text)[:33] == 'I\'m back and I\'m ringin\' the bell'