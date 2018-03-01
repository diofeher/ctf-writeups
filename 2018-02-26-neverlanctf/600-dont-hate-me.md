Don't hate me
=============

```
This Message just might make you crazy. Lets take a stroll through the cipher history time line

New ZIP
-------
But first will need to open the zip! and I am not giving you the password! you will need to crack it. the only hint you get is its all lowercase letters 18char long

Update
------
The second Cipher is a keyed cipher.... one of my favorite ciphers.

I will add hints slowly and those will be encrypted too!
You will need hints to solve So if you solve this with out hints we know you cheated :)
```

1) Solve this question was the turning point for our team. We were 502 points behind first place (hackem - 9875 points) and this question had two hints - one for 10 points and one for 100 points. We took the first hint (-10 points):

```
That Zip is password protected Im telling you that
youwillneverguessme
```

With that, we could unzip the file and there was a ciphered code with dancing men.

2) This is from the book from Arthur Conan Doyle - The adventure of the dancing men. You can encode/decode using this tool:

https://www.dcode.fr/dancing-men-cipher

3) After that, we had a string with a polyalphabetic cipher. We got all members of our team trying to solve with different decoders, but what it worked was a vigenere key using `NeverlanCtf` as key.

http://rumkin.com/tools/cipher/vigenere.php

4) The next text had a big tip on how to solve the next puzzle. 

```
xfmplgijpbjqdhrlmnubkcpghfwxuvajkcvhgfzwr
aeasmgjavjjxkbjcdkedfzlvwqnmyzyafvvrplqfk
ztmbfmedtdvcsgdbhrajqgomhedokvrpsoescxfmp
lgijpbjqdhrlmnubkcpghfwxuvajkcvhgfzwraeas
mggavjjxkxjcdkedfzlvwqnmyzyafvvrplqfkztmb
fmedtdvcsgdbhrajqgomhedokvrpsoesctypemrot
orIrotorIIrotorIIIpositiononepositiontwop
oisitononeukwtypeb
```

In the end, you can see rotor I, etc... We solved using https://cryptii.com/enigma-machine

```
enigmawasoneofthehardestcodestocrackthankstoalanturingandhisteamwenowhavetoolstolearnityourflagisalanturingmadeamachinedngbdetewfakllekolhrpaxybpkzmtdsbadtcyfekvutnpwzbfprmpjwpagvtcvrkzjsubcovpdxbksavjhskohfnammpvazajfzzvimjnodteshvfgpsetfhjhp
->
enigma was one of the hardest codes to crack thanks to alan turing and his team we now have tools to learn it your flag is alan turing madea machine 
dngbdetewfakllekolhrpaxybpkzmtdsbadtcyfekvutnpwzbfprmpjwpagvtcvrkzjsubcovpdxbksavjhskohfnammpvazajfzzvimjnodteshvfgpsetfhjhp
```

Flag is `alanturingmadeamachine` 