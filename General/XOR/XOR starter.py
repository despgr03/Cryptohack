from operator import xor
from Crypto.Util.number import *
import re

t='label'
t2=''
#for each character in t, we convert it to the ascii number and then we do xor the number with the number 13 and the number we turn it into a character
for i in t:
    t2+=chr(xor(ord(i),13))
print(t2)

