from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD 
from sympy import primefactors 
e = 3 
n = 742449129124467073921545687640895127535705902454369756401331 
n1=primefactors(n) 
# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good 
while True: 
    p = n1[0] 
    q = n1[1] 
    phi = (p - 1) * (q - 1) 
    d = inverse(e, phi) 
    if d != -1 and GCD(e, phi) == 1: 
        break 
 
n = p * q 
flag = b"XXXXXXXXXXXXXXXXXXXXXXX" 
pt = bytes_to_long(flag) 
ct = pow(pt, e, n) 
ct = 39207274348578481322317340648475596807303160111338236677373 
print(f"n = {n}") 
print(f"e = {e}") 
print(f"ct = {ct}") 
pt = pow(ct, d, n) 
decrypted = long_to_bytes(pt) 
print(decrypted) 
assert decrypted == flag

#since the file already gives us the N , e and ct , the only thing that lefts to find are the prime numbers p and q that p*q=N
#we use the method primefactors to find them and the d we calculate it since we know the p and q
