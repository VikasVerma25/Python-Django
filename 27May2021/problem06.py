def fact(f):
    if f == 1:
        return 1
    else:
        return f*fact(f-1)

print(fact(int(input("Enter Number: "))))