a=int(input("Enter a number:"))
b=int(input("Enter a number:"))

# while(b!=0):
#     a=b
#     b=a%b#pyhton will read code line by line bcz it is interpreter language so it will give us incorrect value..
# print(b)


while(b!=0):
   a,b = b, a%b
print(a)
    
