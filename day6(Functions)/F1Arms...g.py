n=int(input("enter a nbr:"))
m=n
def Armstrong(n):
    sum=0
    while(n>0):
        digit = n%10
        sum += (digit)**3
        n=n//10
    return sum
res=Armstrong(n)
if(res==m):
    print("yes it is Armstrong nbr..")
else:
    print(" it is not Armstrong..")
