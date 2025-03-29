n=int(input("enter a nbr:"))
m=n
sum=0
while(n>0):
    digit = n%10
    sum += (digit)**3
    n=n//10
if(sum==m):
    print("yes it is Armstrong nbr..")
else:
    print(" it is not Armstrong..")
