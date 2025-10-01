import math

def size(a):
    rslt=0
    for i in range(0,len(u)):
        rslt+=a[i]**2
    rslt=math.sqrt(rslt)
    return rslt

def size1(v1,v2):
    rslt=0
    for i in range(0,len(v1)):
        rslt+=v1[i]*v2[i]
    return rslt
def size2(a):
    rslt=0
    for i in range(0,len(u)):
        rslt+=a[i]**2
    return rslt

v = (846835985,9834798552)
u = (87502093,123094980)
v=list(v)
u=list(u)
size(v)
size(u)

if(size(v)>size(u)):
    tmp=v
    v=u
    u=tmp
m=size1(u,v)/size2(v)
m=round(m)
while(m!=0):
    for i in range(0,len(u)):
        u[i]=u[i]-m*v[i]
    m=size1(u,v)/size2(v)
    m=round(m)
print(size1(u,v))
print(u,v)

#we implemeted the Gaussian Lattice Reduction algorithm they way they described
