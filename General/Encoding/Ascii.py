import base64
from Crypto.Util.number import *

#for each number in the array that depicts an ascii character,we convert it using the chr() array.
t=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for i in t:
    print(chr(i),end='')

