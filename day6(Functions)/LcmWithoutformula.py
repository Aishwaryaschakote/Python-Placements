a=int(input("Enter a number:"))
b=int(input("Enter a number:"))

m_nbr= max(a,b)
while True:
    if m_nbr%a==0 and m_nbr%b==0:
        print("lcm is",m_nbr)
        break
    m_nbr+=1