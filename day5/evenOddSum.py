n=int(input("Enter n:"))
even_sum=0
odd_sum=0
for i in range(1,n+1):
    if(i%2==0):
        even_sum += i
    else:
        odd_sum += i
print(f" Even sum is {even_sum}")
print(f" Odd sum is {odd_sum}")