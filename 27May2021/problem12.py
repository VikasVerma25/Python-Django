n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))

if n1 > n2:
    if n1 > n3:
        m = n1
    else:
        m = n3
else:
    if n2 > n3:
        m = n2
    else:
        m = n3
print("Maximum = ", m)