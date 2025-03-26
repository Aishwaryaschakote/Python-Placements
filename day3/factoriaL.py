n=int(input("enter n:"))
fact=1
fac=1
for i in range(n,0,-1):
    fact= fact*i
print(fact)
print("*********")
for i in range(1,n+1):
    fac= fac*i
    print(f"{i}*",end=" ")
print(f"={fac}")