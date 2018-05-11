from matasano import xor_strings

def encrypt_repeated_xor(text, key):
    output = ''
    for i, c in enumerate(text):
        indice = i % len(key)
        output += '{:02x}'.format(ord(c) ^ ord(key[indice]))
    return output

text = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

result = encrypt_repeated_xor(text, 'ICE')
assert result == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
