b=input("b:")
dec=0
j=0
for i in range(len(b)-1,-1,-1):

   dec+=int(b[i])*(2**j)

   j+=1

   print(dec)
