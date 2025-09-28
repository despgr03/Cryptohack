from operator import xor 
from Crypto.Util.number import * 

KEY1='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313' 
KEY2KEY1='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e' 
KEY2KEY3='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1' 
FLAGKEY1KEY3KEY2='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf' 
#we already have the value of key1 , so in order to get the key2 we do key1key2XORkey1 because key1XORkey=0 so this gives us the key2
#we do the same to get key3 but we xor with ke2
#since the flag is flagkey1key2key3, we do xor with every key and that leaves us with the flag
key1=bytes.fromhex(KEY1) 
key2=bytes.fromhex(KEY2KEY1) 
key1=bytes_to_long(key1) 
key2=bytes_to_long(key2) 
key2=xor(key1,key2) 
key3=bytes.fromhex(KEY2KEY3) 
key3=bytes_to_long(key3) 
key3=xor(key3,key2) 
flag=bytes.fromhex(FLAGKEY1KEY3KEY2) 
flag=bytes_to_long(flag) 
flag=xor(flag,key1) 
flag=xor(flag,key2) 
flag=xor(flag,key3) 
flag=long_to_bytes(flag) 
print(flag)

#solution:crypto{x0r_i5_ass0c1at1v3}
