# 1. Create a class cal1 that will calculate sum of three numbers. 
# Create setdata() method which has three parameters that contain numbers. 
# Create display() method that will calculate sum and display sum.
print("problem 1 =>")
class cal1:
    def __init__(self):
        print("Object Created")

    def setdata(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def display(self):
        print(self.a + self.b + self.c)

callobj = cal1()
callobj.setdata(10,20,30)
callobj.display()

# 2. Create a class cal2 that will calculate area of a circle. Create setdata() 
# method that should take radius from the user. Create area() method 
# that will calculate area . Create display() method that will display area .
print("problem 2 =>")
class cal2:
    def __init__(self):
        print("Object Created")

    def setdata(self):
        self.r = float(input("Enter radius: "))

    def area(self):
        self.area = 3.14*(self.r**2)

    def display(self):
        print(self.area)

cal2obj = cal2()
cal2obj.setdata()
cal2obj.area()
cal2obj.display()

# 3. Create a class cal3 that will calculate simple interest. Create 
# constructor method which has three parameters .Create calInterest() 
# method that will calculate Interest . Create display() method that will 
# display Interest.
print("problem 3 =>")
class cal3:
    def __init__(self, p, t, r):
        self.p = p
        self.r = r
        self.t = t

    def calInterest(self):
        self.interest = float(self.p*self.r*self.t/100)

    def display(self):
        print("Simple Interest:", self.interest)

cal3obj = cal3(1000, 2, 4.5)
cal3obj.calInterest()
cal3obj.display()

# 4. Create a class cal4 that will calculate square of a number. Create 
# setdata() method which has one parameters that contain number. 
# Create display() method that will calculate sum.(Function should 
# return value)
print("problem 4 =>")
class cal4:
    def setdata(self, num):
        self.num = num

    def display(self):
        return self.num**2

cal4obj = cal4()
cal4obj.setdata(5)
print(cal4obj.display())

# 5. Consider an employee class, which contains fields such as name and 
# designation. And a subclass, which contains a field salary. Write a 
# program for inheriting this relation.
print("problem 5 =>")
class employee:
    def __init__(self, name, des):
        self.name = name
        self.designation = des
class salary(employee):
    def __init__(self, name, des, sal):
        super().__init__(name, des)
        self.salary = sal
    def display(self):
        print(self.name, self.designation, self.salary)
s = salary('Ram','intern', 2000)
s.display()

# 6. Create a class cal5 that will calculate area of a rectangle. Create 
# constructor method which has two parameters .Create calArea() 
# method that will calculate area of a rectangle. Create display() method 
# that will display area of a rectangle.
print("problem 6 =>")
class cal5:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calArea(self):
        self.area = self.l*self.b

    def display(self):
        print("Area of rectangle:",self.area)

cal5obj = cal5(20, 30)
cal5obj.calArea()
cal5obj.display()

# 7. Create a class cal6 that will calculate area of a square. Create setdata() 
# method that should take length from the user. Create area() method 
# that will calculate area . Create display() method that will display area.
print("problem 7 =>")
class cal6:
    def __init__(self):
        print("Object Created")

    def setdata(self):
        self.l = float(input("Enter lenght: "))

    def area(self):
        self.area = self.l**2

    def display(self):
        print("Area of square:",self.area)

cal6obj = cal6()
cal6obj.setdata()
cal6obj.area()
cal6obj.display()

# 8. Write a program with use of inheritance: Define a class publisher that 
# stores the name of the title. Derive two classes book and tape, which 
# inherit publisher. Book class contains member data called page no and 
# tape class contain time for playing. Define functions in the appropriate 
# classes to get and print the details. 
print("problem 8 =>")
class publisher:
    def __init__(self, title):
        self.title = title

class book(publisher):
    def __init__(self, title, pageno):
        super().__init__(title)
        self.pageno = pageno
    
    def print(self):
        print("title:", self.title, "pageno:", self.pageno)

class tape(publisher):
    def __init__(self, title, time):
        super().__init__(title)
        self.time = time

    def print(self):
        print("title:", self.title, "time:", self.time)

book1 = book("ABC", 120)
tape1 = tape("XYZ", "50 min")
book1.print()
tape1.print()

# 9. Create a class called scheme with scheme_id, 
# scheme_name,outgoing_rate, and message_charge. Derive customer 
# class form scheme and include cust_id, name and mobile_no 
# data.Define necessary functions to read and display data.
print("problem 9 =>")
class scheme:
    def __init__(self, scheme_id, scheme_name, outgoing_rate, message_charge):
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.outgoing_rate = outgoing_rate
        self.message_charge = message_charge

class customer(scheme):
    def __init__(self, cust_id, name, mobile_no):
        self.cust_id = cust_id
        self.name = name
        self.mobile_no = mobile_no
    
    def read(self):
        a,b,c,d = input("Enter scheme_id, scheme_name, outgoing_rate, message_charge (space separated):").split()
        super().__init__(a,b,c,d)
    
    def display(self):
        print(f"""
        cust_id: {self.cust_id}
        name: {self.name}
        mobile_no: {self.mobile_no}
        scheme_id: {self.scheme_id}
        scheme_name: {self.scheme_name}
        outgoing_rate: {self.outgoing_rate}
        message_charge: {self.message_charge}
        """)
cust1 = customer(111, "john", 7896552743)
cust1.read()
cust1.display()

# 10.Create a arith class. The class should have a parameterized constructor 
# and methods to add, subtract and multiply two numbers and to return 
# the answers
print("problem 10 =>")
class arith:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1+self.n2
    
    def subtract(self):
        return self.n1-self.n2

    def multiply(self):
        return self.n1*self.n2

arith1 = arith(7, 3)
print(arith1.add())
print(arith1.subtract())
print(arith1.multiply())