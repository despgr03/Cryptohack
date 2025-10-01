p=28151
t=2

for g in range(2,p):
    if(t==0):
        print(g-1)
        break
    for n in range(2,p):
        if(pow(g,n,p)==g):
            #print(g)
            t=1
            break
        else:
            t=0
            
