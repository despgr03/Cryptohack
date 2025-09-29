def modar1(a,b): 
    i=1 
  #3*d≡1mod13 is ((3*d)-1)%13==0 so in order to find the d we increase the i until the condition is satisfied.
    while(True): 
        if((((a*i)-1)%b)==0): 
            break 
        else: 
            i+=1 
    print(i) 
 
modar1(3,13) 

