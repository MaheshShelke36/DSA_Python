#Pattern 1 to 5 increase case

"""n=5
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()"""

#Pattern 5 to 1 in decrease case
"""n=5
for i in range(n,0,-1):
    for j in range (i,0,-1):
        print(j,end=" ")
    print() """   

#Pattern will decrease a last number
n=5
for i in range(1,n+1):
    for j in range (n, i-1,-1):
        print(j,end=" ")
    print()    
