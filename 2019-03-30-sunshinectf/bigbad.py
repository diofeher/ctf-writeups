from bitarray import bitarray

dic = {
    's': bitarray('000'),
    'u': bitarray('0010'),
    '_': bitarray('0011'),
    '0': bitarray('010'),
    'd': bitarray('0110'),
    '9': bitarray('0111'),
    '5': bitarray('1000'),
    'n': bitarray('10010'),
    'h': bitarray('10011'),
    'l': bitarray('10100'),
    'a': bitarray('10101'),
    'e': bitarray('10110'),
    'b': bitarray('10111'),
    '1': bitarray('1100'),
    '{': bitarray('11010'),
    '}': bitarray('11011'),
    'r': bitarray('11100'),
    'c': bitarray('11101'),
    'k': bitarray('11110'),
    '3': bitarray('11111'),
}

from PIL import Image
im = Image.open('img.bmp')
rgb_im = im.convert('RGB')
text = ''
for i in range(146):
    pix = rgb_im.getpixel((i, 0))
    if pix[0] == 255:
        text += '1'
    else:
        text += '0'

print(text)
print(''.join(bitarray(text).decode(dic)))
