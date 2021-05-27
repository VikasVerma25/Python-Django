num = int(input("Enter a number: "))
if num < 100:
    print("Number is less than 100")
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("Number is greater than 100")