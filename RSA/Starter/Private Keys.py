p = 857504083339712752489993810777 
q = 1029224947942998075080348647219 
e = 65537 
N=p*q 
t=(p-1)*(q-1) 
d = pow(e,-1,t) 
print(d) 

#in order to find the d we calculate the e^(-1)%t
