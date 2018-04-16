import nclib
import string

printable = set(string.printable)

nc = nclib.Netcat(('52.212.82.173', 6667))
while True:
    text = nc.recv(256)
    if 'CatchMe' in text:
        print filter(lambda x: x in printable, text)

# CatchMe <d40d35b3>
# CatchMe <063c11244>
# CatchMe <fbf38e9>
# CatchMe <b55074be>