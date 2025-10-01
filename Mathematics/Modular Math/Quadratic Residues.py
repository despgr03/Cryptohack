def quad_res(a,p):
    i=0
    t=0
    for i in range(1,p+1):
        if((i**2-a)%p==0):
            t+=1
            print(a,"is quadratic residue and his square root is:",i) 
    if((i==p or i==0)and t==0): 
        i=0 
        print(a,"is not quadratic residue") 
p = 29 
ints = [14, 6, 11] 

for i in ints: 
    quad_res(i,p)
