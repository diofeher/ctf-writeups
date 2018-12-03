from matasano import *

enc_flag = '1d14273b1c27274b1f10273b05380c295f5f0b03015e301b1b5a293d063c62333e383a20213439162e0037243a72731c22311c2d261727172d5c050b131c433113706b6047556b6b6b6b5f72045c371727173c2b1602503c3c0d3702241f6a78247b253d7a393f143e3224321b1d14090c03185e437a7a607b52566c6c5b6c034047'

m = []
for x in [enc_flag[i:i+2] for i in range(0, len(enc_flag), 2)]:
    m.append( int('0x'+x, 16) )

print m

ciphertext = ''.join([chr(i) for i in m])
print ciphertext
calculate_keysize(ciphertext)