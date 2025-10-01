v = [2,6,3] 
w = [1,0,0] 
u = [7,7,2] 
#3*(2*v - w) ∙ 2*u 
for i in range(0,3): 
    v[i]=2*v[i] 
for i in range(0,3): 
    v[i]=v[i]-w[i] 
for i in range(0,3): 
    v[i]=3*v[i] 
for i in range(0,3): 
    u[i]=2*u[i] 
rslt=0 
for i in range(0,3): 
    rslt+=v[i]*u[i]    
print(rslt) 
