from operator import xor 
state = [ 
    [206, 243, 61, 34], 
    [171, 11, 93, 31], 
    [16, 200, 91, 108], 
    [150, 3, 194, 51], 
] 
 
round_key = [ 
    [173, 129, 68, 82], 
    [223, 100, 38, 109], 
    [32, 189, 53, 8], 
    [253, 48, 187, 78], 
] 
#we use the same method to turn the elements of the matrix into its ascii characters
def matrix2bytes(matrix): 
    t="" 
    for i in matrix: 
        for j in i: 
            t+=chr(j) 
    return t 
 #we xor every element of each table with each other
def add_round_key(s, k): 
    t=s 
    for i in range(0,len(s)): 
        for j in range(0,len(s)): 
            t[i][j]=xor(s[i][j],k[i][j]) 
    return t 
 
print(matrix2bytes(add_round_key(state, round_key)))

