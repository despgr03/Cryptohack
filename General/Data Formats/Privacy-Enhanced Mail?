from Crypto.PublicKey import RSA
from Crypto.Util.number import *

#we downloaded the file and we used the RSA.importKey() method to read the key.
f = open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a (1).pem','r')
data = f.read()
print(data)
key=RSA.importKey(data)
print(key.d)

f.close()

