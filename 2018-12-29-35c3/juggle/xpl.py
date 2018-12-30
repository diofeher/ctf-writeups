# coding: utf-8
import os
import subprocess
import textwrap
import time

cmd = 'xalan -xsl chall.xslt < chall.xml'

con1 = subprocess.Popen('nc 35.246.237.11 1 < input1.xml', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
con2 = subprocess.Popen('nc 35.246.237.11 1'.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
output = con1.communicate()[0]
con2.stdin.write('<?xml version="1.0"?>')
con2.stdin.flush()

pnrg = output[50:101].strip()
print 'PNRG', len(pnrg), pnrg

drinks = []
for n in textwrap.wrap(pnrg, 10):
    drinks.append("<drinks>%s</drinks>" % n)

print 'drinks', drinks

inp2 = '''<meal>
<course>
    <plate><Борщ/></plate>
    <plate><Борщ/></plate>
    <plate><Борщ/></plate>
    <plate><Борщ/></plate>
    <plate><Борщ/></plate>
    <plate><दाल/></plate>
    <plate><宫保鸡丁/></plate>
    <plate><दाल/></plate>
</course>
<state>
%s
</state>
</meal>
''' % ''.join(drinks)

for line in inp2.split('\n'):
    con2.stdin.write(line)
con2.stdin.flush()
print con2.communicate()[0]
