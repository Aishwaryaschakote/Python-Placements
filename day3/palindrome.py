#write a program to check a string is palindrome or not
str=input("Enter a string:")
print(str)
r_str=str[::-1]
if(r_str==str):
    print(f"{str} is a palindrome!!")
else:
    print(f"{str} is not a palindrome!!")