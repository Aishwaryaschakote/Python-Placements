def add(a=5,b=10):
    return a+b

print(add())

# def even_sum1():
#     even_sum=0
#     even_sum += i
#     return print(f" Even sum is {even_sum}")

# def odd_sum1():
#     odd_sum=0
#     odd_sum += i
#     return print(f" Odd sum is {odd_sum}")

# n=int(input("Enter n:"))
# for i in range(1,n+1):
#     if(i%2==0):
#         print(even_sum1())
#     else:
#         print(odd_sum1())

n=int(input("Enter n:"))
def program(n):
    even_sum=0
    odd_sum=0
    for i in range(1,n+1):
        if(i%2==0):
            even_sum += i
        else:
            odd_sum += i
    print(f" Even sum is {even_sum}")
    return   print(f" Odd sum is {odd_sum}")

