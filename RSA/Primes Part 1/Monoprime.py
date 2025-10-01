from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD 
from sympy import primefactors 
e = 65537 
n = 171731371218065444125482536302245915415603318380280392385291836472299752747934607246477508507827284075763910264995326010251268493630501989810855418416643352631102434317900028697993224868629935657273062472544675693365930943308086634291936846505861203914449338007760990051788980485462592823446469606824421932591 
 
n1=primefactors(n) 
# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good 
while True: 
    p = n1[0] 
    q = n1[0] 
    phi = (p - 1)  
    d = inverse(e, phi) 
    if d != -1 and GCD(e, phi) == 1: 
        break 
 
#n = p * q 
d = pow(e,-1,phi) 
flag = b"XXXXXXXXXXXXXXXXXXXXXXX" 
pt = bytes_to_long(flag) 
ct = pow(pt, e, n) 
ct = 161367550346730604451454756189028938964941280347662098798775466019463375610700074840105776873791605070092554650190486030367121011578171525759600774739890458414593857709994072516290998135846956596662071379067305011746842247628316996977338024343628757374524136260758515864509435302781735938531030576289086798942   
print(f"n = {n}") 
print(f"e = {e}") 
print(f"ct = {ct}") 
 
pt = pow(ct, d, n) 
decrypted = long_to_bytes(pt) 
print(decrypted) 
assert decrypted == flag

#they gives us the N, e, and the ciphertext and now we know that the number N is a product of one prime number so using the primefactor() method we find the prime number p and we calculate the d as (p-1)
#since now we have everything we need we can decrypt the ciphertext
