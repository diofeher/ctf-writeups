from decimal import *
from binascii import hexlify
from binascii import unhexlify
from math import ceil, log10
from sys import argv

def q():
    getcontext().prec+=5;
    L,t,s,n,k,d,K=0,Decimal(3),3,1,0,0,24
    while s!=L:L=s;n,k=n+k,k+8;d,K=d+K,K+32;t=(t*n)/d;s+=t
    getcontext().prec-=5
    return +s
Q=q()

# print 'Q', Q

def str_base(number, base):
   (d,m) = divmod(number,len(base))
   if d > 0:
      return str_base(d,base)+base[m]
   return base[m]

def s(x):
    # print 'x: ', x
    getcontext().prec+=5;
    i = 1
    L = 0
    s = x
    f = 1
    n = x
    S = 1
    while s != L:
        L = s
        i += 2
        f = f * i * (i-1)
        n *= x**2
        S *= -1;
        s += n / f * S
        # print 'i', i
        # print 'L', L
        # print 's', s
        # print 'f', f
        # print 'n', n
        # print 'S',S
    getcontext().prec-=5
    # print 's: ', s
    return +s

def us(s):
    getcontext().prec+=5;
    s = -s
    # print 's: ', s
    S = 1
    i = 55
    x = s
    f = 12696403353658275925965100847566516959580321051449436762275840000000000000
    L = s
    n = Decimal(-6.126234874598127134235397672509977306625889239842906809446348152703074332762529010946073E-18)
    while i > 3:
        L -= n / f * S
        S *= -1;  #OK
        n /= s ** 2  #OK
        # x = s
        f = f / i / (i-1)  #OK
        i -= 2;  #OK
        x = L
        # print 'i', i
        # print 'L', L
        # print 's', s
        # print 'x', x
        # print 'f', f
        # print 'n', n
        # print 'S',S
    # print 'x:', +x

    getcontext().prec-=5;
    # print 'x: ', x
    return +x

def encrypt(text):
    getcontext().prec=int(ceil(len(text)*2.40823996531))+1;
    print 'Text:', text
    func1 = long(hexlify(text),16)
    print 'Func2: ', func1
    func2 = '0.'+str(func1)
    func3 = Decimal(func2)*Q-Q/Decimal(2)  # func9 = Decimal(y) * Q -Q / Decimal(2)
    print 'Func3: ', func3
    # func305 = 
    # print 'Func3.5: ', func305
    func306 = s(func3) ** 2
    print 'Func4: ', func306
    func31 = Decimal(1) - func306  # 12 = Decimal(1) - x -> 12 + x = Decimal(1) -> x = Decimal(1) - 12 
    func35 = (func31).sqrt()
    # print 'Func4.5: ', func35
    print 'Func5: ', func35
    func4 = str(func35)[2:]
    func5 = hex(long(func4))
    ret = str(func5)[2:-1]
    print 'Ret: ', ret
    print 'Encrypted: ', unhexlify(ret[:-1])
    print 'Decrypt: ', str_base(long(hexlify(text),16), '0123456789abcdef')
    return ret


def decrypt(text):
    getcontext().prec=int(ceil(len(text)*2.40823996531))+1;
    # print 'Encrypted: ', text
    ret = hexlify(text)
    print 'Ret: ', ret
    lamb2 = '0x%s' % ret
    lamb = int(lamb2, 16)
    print lamb
    func3 = '0.%s' % lamb
    print 'Func5: ', Decimal(func3)
    func35 = Decimal(func3) ** 2
    # print 'Func4.5: ', func35
    func31 = Decimal(1) - Decimal(func35)
    print 'Func4: ', func31
    func305 = us(func31.sqrt())
    print 'Func3: ', func305
    func8 = (func305 + Q / Decimal(2)) / Q
    func11 = str(func8)[2:]
    print 'Func2: ', func11
    func10 = unhexlify(str_base(int(func11), '0123456789abcdef'))
    print 'Text: ', func10
    return func10

A=hexlify("Usage: "+argv[0]+" <string>") if len(argv)!=2 else encrypt(argv[1])
f=open("out.txt",'w')
f.write(unhexlify(A[:-1] if len(A)%2==1 else A))  # remove the last char if is odd
f.close()

f=open("out.txt",'r')
decrypt(f.read())
f.close()

f=open("out1.txt",'r')
print decrypt(f.read())
f.close()