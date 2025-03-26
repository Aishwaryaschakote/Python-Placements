# n=int(input("Enter n:"))
#n=5
# for i in range(1,n+1):
#     print(' * '*i)

#METHOD 1   
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#METHOD 2
for i in range(1,5+1):
    print(' * '*i)
for i in range(6,0,-1):
    print(" * "*i)