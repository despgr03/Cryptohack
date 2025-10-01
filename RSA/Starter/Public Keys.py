p=17 
q=23 
N=p*q 
r=(12**65537)%N 
print(r)

#in order to encrypt a number with the RSA encryption method (a^e)modN where N is the product of two prime numbers ,a the number we want to encrypt and e an exponent 
