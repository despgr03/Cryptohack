i=1 
while(True): 
if(i%5==2 and i%11==3 and i%17==5): 
print(i) 
break 
else: 
i+=1 
print(i%(935))

#we are trying to find a number x that satisfies these conditions x≡2mod5 ,x≡3mod11,x≡5mod17.meaning we are searching for a number that x≡amod(5*11*17) and that number is x=a.
