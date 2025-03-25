num = int(input("Enter a number: "))

if num > 1 and (num == 2 or num == 3 or num == 5 or num == 7 or 
   (num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0)):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")