def gcd(a,b): 
    max=0 
    min=0 
    poll=0 
    upo=0 
    s1=1 
    s2=0 
    t1=0 
    t2=1 
    tmps=0 
    tmpt=0 
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
        poll=(max-upo)//min 
        max=min 
        if(upo>0): 
            min=upo 
            tmps=s1-poll*s2 
            s1=s2 
            s2=tmps 
            tmpt=t1-poll*t2 
            t1=t2 
            t2=tmpt   
    if(b>a): 
        tmps,tmpt=tmpt,tmps
    print(max) 
    print('u=',tmps) 
    print('v=',tmpt) 
gcd(26513,32321)



#for the solution we followed the Extended Euclidean algorithm that is shown in wikipedia.
#solution: -8404

