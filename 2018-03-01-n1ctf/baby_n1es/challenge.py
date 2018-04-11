from N1ES import N1ES, ap
import base64
key = "wxy191iss00000000000cute"
n1es = N1ES(key)
flag = "N1CTF{aj9zfgggb34ggggggg1111111****************}"
cipher = n1es.encrypt(flag)
print ap(cipher)
print
# print ap('HRlgC2ReHW1/WRk2DikfNBo1dl1XZBJrRR9qECMNOjNHDktBJSxcI1hZIz07YjVx')

# b64decode
n1es.decrypt("HRlgC2ReHW1/WRk2DikfNBo1dl1XZBJrRR9qECMNOjNHDktBJSxcI1hZIz07YjVx")