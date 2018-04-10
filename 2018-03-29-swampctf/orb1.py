from string import translate, maketrans

story = """
The monastery of the priests of Pelor was under siege by a mysterious group.  
You responded quickly to the distress signal and managed to help stabilize the 
situation while hearing a message in retreat "It is written, you will all serve The 
Ever Shining Army of the Crystal Throne!"  Sifting through the wreckage you find a 
fallen enemy wearing purple and black robes with a silver breast plate embossed with an 
image of a purple dragon.  One of the monks, robed in brilliant yellow and orange, shakes her head solemnly.  

Another monk's eyes perk up and you notice them gazing at a rectangular impression in the sleeve of the figure.
Upon inspection you discover a compartment with some potions, pendants, money, and an old book.  The book's leather binding seems
vaguely familiar but still quite different from any leather you've ever seen.  Thumbing through it you realize it is some sort of
notebook.  At first it seems to be talking of some forgotten place and notice a few passages written in some cryptic language
adhered to several pages followed by a torn page or two.  After these passages, the rest of the text appears to be increasingly
indecipherable and at one point there are pages of numbers.

You were curious about the passages and decided to try your hand at decrypting them.  Let us hope it is not as the priests 
seem to fear.
"""

cipher = "flagSTRANGE2thin9zWorLdZ"
plain_ = "abcdFGHIJKLmnopqrsTuvWxY" # you just order the plain text and move cipher around
trantab = maketrans(cipher, plain_)

crypttext = '''
gh2AtAht hS zRfghLz ftg otozofE WRAtTz

"WhdAa gh2fAt hS gf9G AEEozAht
Eftg WRfW zR9hogz EhfWRAtT EATRW
lhotgf9Z hS Lh9Egz otGthLt"

Eftg hS zRfghLz, f WLAEATRW gh2fAt WRfW Az f gf9G 2A99h9, h9 ahiZ, hS ho9 Lh9Eg. f ihAtW hS lEATRW ftg ah99hzAht, f gh2fAt hoW hS zZta, f Eftg LAWR Rh99h9z 9ATRW lZ Zho ftg Zho ght'W GthL.

f9WAzftz hS f WRfo2fWo9TAafE GAtg gh thW ozofEEZ a9hzz AtWh Eftgz hS zRfghL Sh9 At zoaR gh2fAtz ft otGthLt Rh99h9 Az zfAg Wh Eo9G.  f99ArfE fELfZz l9AtTz flhoW gAzzhEoWAht hS fziA9fWAhtz Sh9 zRfghLz noAaGEZ zLfEEhL zhoEz hS EATRW At f 2ZzWAa A2ihzzAlAEAWZ.  f zhEAWf9Z foTo9Z Lfz i9hhS: GAtTgh2z LAEE SfEE fz ahtNo9fWAht hS zRfghL TEhh2z 2AggfZ LAWR gf9G 2fEAaAhoz ShT, f Eo2Athoz aRf92 LAEE afzW f 9fZ WRfW fTfAt fEATtz ho9 Lh9Eg.'''
print '='*80
print crypttext
print '='*80
print crypttext.translate(trantab)