
from pwn import * 
t='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d' 
t=bytes.fromhex(t) 
t1='' 
t2="crypto" 
t2=bytes(t2,'utf-8') 
#since a byte is 8 bits, and 2^8 is 256 that means a byte can represent 256 number, from 0 to 255.
#we xor with each number until we find the value "crypto" since keyflagXORkey gives us the flag.
for i in range(0,256): 
    t1=xor(t,i) 
    if (t1.find(t2)==0): 
        print(t1) 
        break 

