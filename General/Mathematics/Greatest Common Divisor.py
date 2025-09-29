#this is a method to find the greatest common divisor among numbers.
#we divide the numbers from the greater to the minimum and do the divison. the remainder of the division gets into a variable and the new max becomes the min.
#if the remainder is 0, that means that the min(the new max) divided perfectly the numbers and this is the greatest divisor amongst the two given numbers.
#if not , the new min becomes the remainder and we do the same until it is 0.
def gcd(a,b):
    max=0 
    min=0 
    upo=a
    if(a>b): 
        max=a 
        min=b 
    else: 
        max=b 
        min=a 
    while(upo>0): 
        upo=max%min 
        max=min 
        if(upo>0): 
            min=upo 
    print(max) 
 
gcd(66528,52920) 

