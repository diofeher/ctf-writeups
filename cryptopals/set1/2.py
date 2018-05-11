def xor_strings(text1, text2):
    lst = [chr(ord(a) ^ ord(b)) for a, b in zip(text1.decode('hex'), text2.decode('hex'))]
    return ''.join(lst).encode('hex')

# the kid don't play
assert xor_strings('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965') == '746865206b696420646f6e277420706c6179'
