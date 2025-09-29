def modar1(a,b): 
    i=1 
  #the a≡bmodm is (a-b)%m==0. In order to find the x and y , we icrease the i until the condition is satisfied
    while(True): 
        if(((a-i)%b)==0): 
            break 
        else: 
            i+=1 
    print(i) 
 
modar1(11,6) 
modar1(8146798528947,17) 

#solution: 4
