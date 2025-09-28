import base64
from Crypto.Util.number import *

#fisrt we convert from hex to bytes and then from bytes to base64
t2='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
t3=bytes.fromhex(t2)
t4=base64.b64encode(t3)
print(t4)

#solution: crypto/Base+64+Encoding+is+Web+Safe/
