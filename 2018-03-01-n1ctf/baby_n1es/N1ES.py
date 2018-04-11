# -*- coding: utf-8 -*-
import base64

# def ap(n):
#     for i in range(1):
#         st = ":".join(str(ord(c)) for c in n[i*16: 16*(i+1)]).split(":")
#         print st[:8], st[8:len(st)]

def permutate(table, block):
	return list(map(lambda x: block[x], table))

def string_to_bits(data):
    data = [ord(c) for c in data]
    l = len(data) * 8
    result = [0] * l
    pos = 0
    for ch in data:
        for i in range(0,8):
            result[(pos<<3)+i] = (ch>>i) & 1
        pos += 1
    return result

s_box = [54, 132, 138, 83, 16, 73, 187, 84, 146, 30, 95, 21, 148, 63, 65, 189, 188, 151, 72, 161, 116, 63, 161, 91, 37, 24, 126, 107, 87, 30, 117, 185, 98, 90, 0, 42, 140, 70, 86, 0, 42, 150, 54, 22, 144, 153, 36, 90, 149, 54, 156, 8, 59, 40, 110, 56,1, 84, 103, 22, 65, 17, 190, 41, 99, 151, 119, 124, 68, 17, 166, 125, 95, 65, 105, 133, 49, 19, 138, 29, 110, 7, 81, 134, 70, 87, 180, 78, 175, 108, 26, 121, 74, 29, 68, 162, 142, 177, 143, 86, 129, 101, 117, 41, 57, 34, 177, 103, 61, 135, 191, 74, 69, 147, 90, 49, 135, 124, 106, 19, 89, 38, 21, 41, 17, 155, 83, 38, 159, 179, 19, 157, 68, 105, 151, 166, 171, 122, 179, 114, 52, 183, 89, 107, 113, 65, 161, 141, 18, 121, 95, 4, 95, 101, 81, 156, 17, 190, 38, 84, 9, 171, 180, 59, 45, 15, 34, 89, 75, 164, 190, 140, 6, 41, 188, 77, 165, 105, 5, 107, 31, 183, 107, 141, 66, 63, 10, 9, 125, 50, 2, 153, 156, 162, 186, 76, 158, 153, 117, 9, 77, 156, 11, 145, 12, 169, 52, 57, 161, 7, 158, 110, 191, 43, 82, 186, 49, 102, 166, 31, 41, 5, 189, 27]

def generate(o):
    k = permutate(s_box,o)
    b = []
    for i in range(0, len(k), 7):
        b.append(k[i:i+7] + [1])
    c = []
    for i in range(32):
		pos = 0
		x = 0
		for j in b[i]:
			x += (j<<pos)
			pos += 1
		c.append((0x10001**x) % (0x7f))
    return c


def ap(n):
    return ":".join(str(ord(c)) for c in n)

def round_add(a, b):
    f = lambda x, y: x + y - 2 * (x & y)
    res = ''
    print 'A:', ap(a), 'B', b
    for i in range(len(a)):
        func = f(ord(a[i]), ord(b[i]))
        res += chr(func)
    print ap(res)
    return res


def unround_add(a, b):
    f = lambda x, y: x + y - 2 * (x & y)
    res = ''
    print 'A:', ap(a), 'B', b    
    for i in range(len(a)):
        ch = ord(a[i])
        b2 = ord(b[i])
        a2 = 0
        while True:
            if f(a2, b2) == ch:
                # print 'achou', count
                break
            else:
                a2 += 1
        res += chr(a2)
    return res

class N1ES:
    def __init__(self, key):
        if (len(key) != 24 or isinstance(key, bytes) == False ):
            raise Exception("key must be 24 bytes long")
        self.key = key
        self.gen_subkey()

    def gen_subkey(self):
        o = string_to_bits(self.key)
        k = []
        for i in range(8):
	        o = generate(o)
        	k.extend(o)
        	o = string_to_bits([chr(c) for c in o[0:24]])
        self.Kn = []
        for i in range(32):
            self.Kn.append(map(chr, k[i * 8: i * 8 + 8]))
        # print 'KN', self.Kn
        return 

    def encrypt(self, plaintext):
        # print "Plaintext", plaintext
        if (len(plaintext) % 16 != 0 or isinstance(plaintext, bytes) == False):
            raise Exception("plaintext must be a multiple of 16 in length")
        res = ''
        for i in range(len(plaintext) / 16):
            # print i
            block = plaintext[i * 16:(i + 1) * 16]
            L = block[:8]
            # print 'L', L
            R = block[8:]
            # print 'R', R
            # print 'L:', ap(L), 'R:', ap(R)
            for round_cnt in range(32):
                L, R = R, (round_add(L, self.Kn[round_cnt]))
                print 'L:', ap(L), 'R:', ap(R), 'round_cnt:', round_cnt
            L, R = R, L
            print 'L:', ap(L), 'R:', ap(R)
            res += L + R
            # print 'Res', ap(res)
        return res

    def decrypt(self, res):
        print '-' * 56
        print 'DECODE --------'
        res = base64.b64decode(res)
        print 'len:', len(res)
        print ap(res)
        flag = ''
        for i in range(len(res) / 16):
            block = res[i * 16:(i + 1) * 16]
            L = block[:8]
            R = block[8:]
            # L, R = R, L
            for round_cnt in reversed(range(32)):
                L, R = R, (unround_add(L, self.Kn[round_cnt]))
                print 'L:', ap(L), 'R:', ap(R), 'round_cnt:', round_cnt
            L, R = R, L
            flag += L + R
        print 'FLAG:', ap(flag)
        print 'FLAG:', flag
            
                