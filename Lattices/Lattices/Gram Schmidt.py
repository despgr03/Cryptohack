#import math

def size(v):
    rslt=0
    for i in range(0,len(v)):
            rslt+=v[i]**2
    #rslt=math.sqrt(rslt)
    return rslt
                   

def size1(v1,v2):
    rslt=0
    for i in range(0,len(v1)):
        rslt+=(v1[i])*(v2[i])
    return rslt
                   
v1 = (4,1,3,-1)
v2 = (2,1,-3,4)
v3 = (1,0,-2,7)
v4 = (6, 2, 9, -5)
w1=list(v1)
w2=list(v2)
w3=list(v3)
w4=list(v4)


for i in range(0,len(v2)):
    w2[i]=round((size1(w1,v2)/size(w1))*w1[i],5)
    w2[i]=round(v2[i]-w2[i],5)

for i in range(0,len(v3)):
    w3[i]=round((size1(w1,v3)/size(w1))*w1[i]+(size1(w2,v3)/size(w2))*w2[i],5)
    w3[i]=round(v3[i]-w3[i],5)
    
for i in range(0,len(v4)):
    w4[i]=round((size1(w1,v4)/size(w1))*w1[i]+(size1(w2,v4)/size(w2))*w2[i]+(size1(w3,v4)/size(w3))*w3[i],5)
    w4[i]=round(v4[i]-w4[i],5)


print(w4)

#we implemented the  Gram-Schmidt algorithm that was described
