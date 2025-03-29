a=int(input("Enter a number:"))
b=int(input("Enter a number:"))


def gcd(a,b):
    while(b!=0):
        a,b=b,a%b
    return a 

# print(gcd(a,b))

lcm=(a*b)/(gcd(a,b))
print(lcm) #lcm using formula..
