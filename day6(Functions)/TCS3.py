
n = int(input("Enter the number of terms: "))

def fibo(n):
    sum=0
    # First two terms
    a, b = 0, 1
    for i in range(n):
        # print(a, end=" ")
        sum+=a
        a, b = b, a + b
        
    return sum
print(fibo(n))