Using Kali Linux to run xpl.py (doesn't work on OS X)

1) First you have to use xalan to test this exploit locally by running the following command:

xalan -xsl chall.xslt < chall.xml

2) PRNG was based in seconds, so you could open two connections at the same time, get the number, and use that on the input of the other connection, thus, receiving the flag.

35C3_The_chef_gives_you_his_compliments