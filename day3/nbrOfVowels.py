#count the nbr of vowels in the string

#METHOD 1
# str=input("enter string:")
# c=0
# for ch in str:
#     if((ch=='a')| (ch=='e') |(ch=='u') |(ch=='o') |(ch=='i')|(ch=='A')| (ch=='I') |(ch=='U') |(ch=='O') |(ch=='E')):
#         c = c+1
# print(c)   

#METHOD 2
str=input("enter string:")
count=0
vowels="AEIOUaeiou"
for ch in str:
    for vo in vowels:
        if(ch==vo):
            count +=1     
print(count)     
      
      