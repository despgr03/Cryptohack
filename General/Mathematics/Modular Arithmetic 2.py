def gcd(a,b): 
    max=0 
    min=0 
    upo=0 
    if(a>b): 
        max=a 
        min=b 
        upo=a 
    else: 
        max=b 
        min=a 
        upo=a 
    while(upo>0): 
        upo=max%min 
        max=min 
        if(upo>0): 
            min=upo 
    return max 
 #according to Fermat's little theorem,if a and p two numbers and p is a prime number and the greatest common divisor of a and p is 1,
#meaning that a number that divides perfectly a and p doesnt exists, then the remainder of the (a**(p-1))%p is 1.
def modar2(a,b): 
    if(gcd(a,b)==1): 
        print(a,"^",(b-1),"mod",b,"=1") 
    else: 
        print("unknown") 
 
modar2(273246787654,65537)

#solution: 1

