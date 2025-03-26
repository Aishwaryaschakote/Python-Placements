s=input("enter a string:")

#METHOD 1
# print(s[::-1])

#METHOD 2
n=len(s)
print(n)
for i in range(n-1,-1,-1):
    print(s[i], end="")

#METHOD 3
# r_str=" "
# for ch in s:
#     r_str = ch+r_str
# print(r_str)