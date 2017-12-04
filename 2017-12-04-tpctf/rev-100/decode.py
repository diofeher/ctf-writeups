from PIL import Image
import pdb
import collections

def decode(colors):
    rand1 = colors[0]
    rand2 = colors[1]
    char = colors[2]
    rand1i = rand1 / 256
    rand2i = rand2 / 256
    char = round(char / 10 / rand2i / rand1i)
    return chr(char)

def decrypt():
    strings = ['']*38
    for i in range(1, 101):
        filename = 'out'+str(i)+'.png'
        im = Image.open(filename)
        px = im.load()
        for i in range(im.size[0]):
            colors = px[i, 0]
            char = decode(colors)
            strings[i] += char
    for i in range(38):
        print(collections.Counter(strings[i]).most_common(1)[0][0], end='')

decrypt()