f=open("output_479698cde19aaa05d9e9dfca460f5443.txt", 'r')  
data= f.read() 
i=data.find('i') 
ints=data[i:] 
p=data[:i] 
p=p[p.find('= ')+2:] 
p=int(p) 
ints=ints[ints.find('[')+1:] 
ints=ints[:ints.find(']')] 
ints=ints.split() 
list1=[] 
for i in ints: 
    list1.append(i[:i.find(',')]) 
list2=[] 
for i in list1: 
    list2.append(int(i))     
f.close() 
 #we check if p satisfies the  p≡3mod4 condition.if yes then we can apply the legendre symbol.
if(p%4==3): 
    for i in list2: 
      #according the legendre symbol if (p−1)/2≡1(modp) then a is a  quadratic residue and his square roots are (+)(-) a^((p+1)//4)​(modp)
        if(pow(i,(p-1)//2,p)==1): 
            print("arithoms",i) 
            print("solution",pow(i,(p+1)//4,p)) 
print("solution",(-1)*(pow(i,(p+1)//4,p)))
