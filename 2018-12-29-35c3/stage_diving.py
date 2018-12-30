# coding: utf-8
import PIL
import os
import zlib
import subprocess
import base64
from PIL import Image
import hashlib

mappings = {
    '49960558f255d456e957144dcde0ae97': 'w',
    '3369a63f47ded2eb4299258708313055': 'c',
    '266bbac0c69dd6abf6c6c85e68e6f18c': 'z',
    '8f9c38143f1a95253f3be47043deaa57': '7',
    '75048edb9a79892a5581c26ebe3cdc50': '9',
    'c593ea020a2997e0d73f7818e5e82897': 'u',
    'a6eaca985826f964de3988cd06d12ee9': 'e',
    'aec7b939453207c887ea553ad00932b9': 'J',
    'acde7c389dc85755db8c53e400183620': 'y',
    'b2ce504315cd1b5118cad248ff99707d': 'A',
    '6426c5aefcdf83d7ba32be2306356342': 'Q',
    '5a900b83598c90f23bef8eda4ed60600': 'g',
    '16d49473ad616379bc16581c0945a1a4': 'P',
    '7f24d1eb7e4cc760ad085b8141680df1': 'p',
    'cc21140df97cbcc0a9c0c227b2cbdd6e': 'G',
    '76a559a26c5cd4f21d733acfcaf29560': 'T',
    'b178784cdbb457910bfde135469c9c81': '3',
    '23b87e5aedb4a01a3dd739af151089c3': 'F',
    '74405fcc56c4fd708454d5c82868fce5': 't',
    '6403bf3fa3ff40a9fc2ca8e1a52ff0a1': 'S',
    '4fc1122c866ad977db19ae97567cfaa4': 'N',
    '34ede503f6d7295d1c779f22af0532d6': 'r',
    '47067eef3b53d53e3feab1c7c6ab03d3': 'Z',
    '3a25ebb37b330a269af2d7a4ddb2c55d': 'o',
    '89883b2b5981ec18804ac1725bb5e82d': 'i',
    'fb0938ceede1e25eeee6e5f9354e5a9a': 'j',
    'ca58046ee740d2bf908c4cca19ce7371': '0',
    '9a278d82485b95aa780dbd9805230959': 'R',
    '56ae1cdae5c5dc472199ba8cef6e057b': '6',
    '52fe5e0efdc91d62d8c86465354d102a': 'E',
    'a573e18b84438ba386bc51be4ef2774b': '+',
    '7e17dd3933fc2b13a594991e91ae8c10': 'K',
    'c39228f4ef074044e027b488ed00087c': 'U',
    '4acc6ad30776ffa6f9fc5283b5ddad1f': 'O',
    '7ea355716a309aec5ab720f45f005753': 'l',
    '46aae9a3b34185f30cdcc9dbd0d4ce2e': 'D',
    '70d6abe842b4b1285e0c29185faf3981': 'M',
    'acd4ff5af1bd41bb8cbe6b4e41244b93': 'd',
    'bf7f9d48158d985d2a5863c9e13ed6fa': 'I',
    '574bbe519eaec037f919df3663c99a07': '4',
    'c82c23c6de91b43621024b8c18dc11eb': 'h',
    '49f05ef711998458e68e96b983c8a9d0': '(',
    'bd71bf0738769f16586bdb75b44f91bf': '_',
    'f8770a13fd79a538c5280450290bce9a': '`',
    'dc9b011bf60d5c4fd35cf9fbdde20519': '@',
    '47041290d61d487c74fe8909ff4e2ffa': '{',
    'ec906b7510c5f265b63fb0f33a50ad71': '>',
    '043de4d1830b4affddb6270cff202a53': ')',
    'e37e97a970c355772ae67e0d175e36eb': '\'',
    '7b8005fb3e0ffe07ab44745cd215b5b2': '\\',
    'dae113e7a9ce633b34f3a2624950309b': '}',
    'a8013907b1c89277a2dac0dce1dc9255': '.',
    'cb43ec05b95d93500fcf25650448ed49': ';',
    '96f5286c9ce1f0d7a4fb67e25493d5db': '*',
    'e90b3cfeeb7bd35d8c2637c92dba232a': '!',
    '68b156f7d33108e1c723b27f8555fb17': '?',
    '7e8987a72044ff273cc5cbef7c15ec67': '|',
    '52370dd4b814306cb07d81e0eba87f12': 'n',
    'af9f6c9abfbe74d69830bd88ed719bd8': '2',
    '458a5e87e0b89054e8a57f622b2d77c2': 'L',
    '9b68dbb56fd58b2a74ae4afffff75e40': 'X',
    'e97c03ecc2127599b565ed918d6aa4e2': 'W',
    'f2d936ab32d28cf3380488707b54ae91': 'B',
    '4eb17b22f75b09daaf3439517584f943': 'q',
    '7ad5f6b26be224fac5107c6616e7fcc7': 'm',
    '6e72284a36cbb964a0fa7fadf101db9f': 'H',
    'c22f655638296cba81cfa85f99c57358': '5',
    'e0ea0ed85ba28e7f27afce8d6aeee675': '/',
    'e3a0715a7ae7a3beec01deb414163f0b': 'a',
    'c78c812c58be1f16c222a95e5a8f3762': '1',
    '00075451736e00439cc7a20c2e408ac0': 'k',
    '61ce36cd612987f212deb3ec746d872d': '=',
    'b8a6245cb36d6b2b1b53cc8e4fe8ad8a': ' ',
    '88cbffb03147e20d736c1427ba9bbc7a': '#',
    '04accf02767a028bc9cdb4008cd16932': '^',
    'a838b6c47a863d756eff831c6fd1ae59': ',',
    'a88225a7df64a2e4d895af52a7f6632d': ' ',
    'f42d6cdefac88e52b5a66b08b24492bf': '"',
    'cdc4b561dc88d32ca4ba20e0ab6c90ee': ']',
    'fdace4731e4624edf812e31e9bd1e74a': 'v',
    '31931ca1e4be14b5195948f0d469b992': 'b',
    'a871d754367830600be1ab28c9e09eb3': 'C',
    '0e8a0c21e32fb7f96b32352f4d08b512': 'Y',
    'c9324de29815171133e4e7c9fc114313': '8',
    'ca2c3a35b38e816712fa628e69997d3b': 'f',
    '72d1f528e3e60ea6a92eebe42b3c40ff': 'x',
    '1bac3ae1e221ab62317a1b1d304ec049': '%',
    '9141b03bd8191459ea2e2f42247ff1c4': '-', 
    'ceb5ce44c5b5aad64ce530d7e472d833': '$',
    '4e444dba7a72a3032dd5eea4749067ba': 'ç',
    'f841f7a95ac041f517bb8c68824d3500': '<',
    'd5b1560524f4f294638a9585f756f72c': '[',
    'fd02272343e420551a8e37e1f5804d96': ':',
    'ba162b386043879ebf2d9c0166b54906': 's',
    '4de10ff846068988e9101e3660298f03': 'V',
}
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/='

def download_image(url):
    print 'URL', url
    os.system('curl %s -s -o download.png' % url)
    img = Image.open('download.png').convert('RGB')
    width,height = img.size
    pix = img.load()
    # img.show()

    with open('download.ppm', 'w') as f:
        f.write('P1\n')
        f.write(str(width*3) + ' ' + str(height) + '\n')
        for i in range(height):
            for j in range(width):
                f.write(' '.join(str(int(k==255)) for k in pix[j, i]) + ' ')
                f.write('\n')

    output = ''
    lines = 32
    columns = 128

    os.system('convert download.ppm pixels.png')
    im = Image.open('pixels.png')
    line_spacing = im.height / lines 
    col_spacing = im.width / columns
    upper = -line_spacing
    lower = 0
    for i in range(lines):
        upper += line_spacing
        lower += line_spacing
        left = 0
        right = col_spacing
        for j in range(columns):
            params = [left, upper, right, lower]
            new_im = im.crop(params)
            hsh = hashlib.md5(new_im.tobytes()).hexdigest()
            char = mappings.get(hsh, '')
            if not char:
                print hsh
                new_im.show()
                import pdb; pdb.set_trace()
            if char in chars:
                output += char
            left += col_spacing
            right += col_spacing
    number = 332
    while True:
        try:
            decoded = base64.b64decode(output[:number])
            return zlib.decompress(decoded)
        except (TypeError, zlib.error), e:
            pass
        number += 1

result = download_image('http://35.207.97.153/')
print result
while True:
    left = result.find('Go to http:')
    if left < 0:
        left = result.find('http')
    else:
        left += 6 
    right = left + 118
    result = download_image(result[left:right].strip())
    print result


# 35C3_this_m1ghT_be_the_f1aG