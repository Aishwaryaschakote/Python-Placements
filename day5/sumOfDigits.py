n=int(input("Enter a number:"))
sum=0
#digit=0

# while(n!=0):
#     digit=n%10
#     sum +=digit
#     n=n//10
    
# print(sum)
#instead of using digit as another variable.. we can do it directly
while(n!=0):
    sum += n%10
    n = n // 10    
print(sum)

    
