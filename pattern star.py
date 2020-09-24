n=int(input("enter a number"))
for i in range(n,-1,-1):
    for j in range (i,n):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()

n=int(input("enter a num"))
for i in range(n,0,-1):
    print("*"*(i).center(2*n))
