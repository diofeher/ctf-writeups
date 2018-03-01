import socket
from PIL import Image
from haishoku.haishoku import Haishoku
import telnetlib
import requests
import time

colors = {
    1: "azul",
    2: "amarelo",
    3: "verde",
    4: "rosa",
    5: "laranja",
    6: "ciano",
    7: "vermelho",
    8: "roxo",
    9: "marrom",
}
def get_code(rgb):
    OFS = 30
    azul = (0, 0, 250)
    amarelo = (251, 251, 4)
    verde = (3, 250, 3)
    rosa = (252, 150, 252)
    laranja = (252, 150, 2)
    ciano = (4, 251, 199)
    vermelho = (248, 2, 2)
    roxo = (199, 1, 252)
    marrom = (150, 74, 3)
    cores = [azul, amarelo, verde, rosa, laranja, ciano, vermelho, roxo, marrom]

    for i, c in enumerate(cores):
        if (rgb[0]+OFS > c[0] and rgb[0]-OFS < c[0]) and (rgb[1]+OFS > c[1] and rgb[1]-OFS < c[1]) and (rgb[2]+OFS > c[2] and rgb[2]-OFS < c[2]):
            print(colors[i+1])
            return i+1

def read_gif(im):
    response = ""
    path = "/tmp/test.jpg"
    try:
        while 1:
            jpg = im.convert("RGB")
            jpg.save(path)
            img = Haishoku.loadHaishoku(path)
            code = get_code(img.dominant)
            response += str(code)
            # print(code); im.show(); time.sleep(1)
            im.seek(im.tell()+1)
    except EOFError:
        pass
    return response

def get_number(code):
    func = (3 * pow(int(code[0]), 9)) * (5 * pow(int(code[1]), 8))
    func2 = pow(int(code[2]), 7) + pow(int(code[3]), 6) - pow(int(code[4]), 5)
    return (func-7*func2) % 13371337

def main():
    nc = telnetlib.Telnet("159.89.46.164", 1337)
    nc.set_debuglevel(100000)
    nc.write(str.encode("start"))
    while True:
        nc.read_until(str.encode("Link: "))
        url = nc.read_until(str.encode(".gif"))
        img = Image.open(requests.get(url, stream=True).raw)
        code = read_gif(img)
        md = str(get_number(code))
        nc.write(str.encode(md))
    # nc.close()

main()
