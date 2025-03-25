a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if(a>b and a>c):
    print(f"{a} is greater among all 3 nbrs")# formatting for printing original value.. of variable
elif(b>a and b>c):
    print(f"{b} is greater among all 3 nbrs")
else:
    print(f"{c} is greater among all 3 nbrs")

print(type(a))

#even or odd