Level 0
=========

ssh bandit0@bandit.labs.overthewire.org -p 2220

pw: bandit0

Level 1
==========

pw: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

echo "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d" | xxd -r -p
-> boJ9jbbUNNfktd78OOpsqOltutMc3MY1

Level 2
==========
cat ./-

-> CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

Level 3
==========
cat ./spaces\ in\ this\ filename

UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

Level 4
==========
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

Level 5
==========
koReBOKuIDDepwhWk7jZC0RTdopnAYKh

Level 6
==========
find . -size 1033c

DXjZPULLxYr17uwoI01bNLQbtFemEgo7

Level 7
==========
find / -size 33c -group bandit6 -user bandit7 2>/dev/null

HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

Level 8
==========
cat data.txt | grep millionth

cvX2JJa4CFALtqS87jk27qwqGhBM9plV

Level 9
==========
sort -n data.txt | uniq -u

UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

Level 10
==========
strings data.txt | grep '==='

truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

Level 11
==========
cat data.txt | base64 -d

IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

Level 12
==========
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

Level 13
==========
cp data.txt /tmp/mydir
xxd -r data.gz > data.tar
tar -xvf data.tar
gzip -d data.gz

8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

Level 14
==========
ssh bandit.labs.overthewire.org -l bandit13 -p 2220

ssh -i sshkey.private localhost -l bandit14

4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

Level 15
==========
telnet localhost 30000

BfMYroe26WYalil77FoDi9qh59eK5xNr

Level 16
==========
