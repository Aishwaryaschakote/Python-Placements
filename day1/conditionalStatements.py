# WAP check the eligibility criteria for voting
# age=18
# if(age>=18):
#     print(" u are eligible for voting..!")
# else:
#     print(" u are not eligible for voting..!")

#########################
# WAP check the eligibility criteria for driving licence
# age=44
# if(age<16):
#     print(" u are  not eligible for learning and driving licences..!")
# elif((16<age) and (age<18)): # elif((16<=age<=18)):
#     print(" u can apply for learning licence..!")
# else:
#     print(" u are  eligible for driving licence..!")
############################

marks=int(input("Emter your marks:"))
if(90<=marks<=100):
    print("A")
elif(80<=marks<=90):
    print("B")
elif(70<=marks<=80):
    print("C")
elif(60<=marks<=70):
    print("D")
elif(marks<60):
    print("FAIL")