n=int(input(" "))
rem=' '
while n:
    rem+=str(n%2)
    n=n//2
print(rem[::-1])
    
