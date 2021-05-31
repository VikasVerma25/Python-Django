# A function is group of related statements
def myfunc():  			# function header
	print("HELLO")
myfunc()      		  # calling function

# function with argument
def myfunc(value):  
	print("HELLO "*value)
myfunc(10)

# function with argument and return statement
def myfunc(name):  
	print("HELLO")
	return name
print(myfunc("XYZ"))

# function with multiple return
def myfunc(num):  
	return num**2, num**3
n, m = myfunc(10)
print("Square", n)
print("Cube", m)

# default and keyword arguments
def myfunc(a , b , c = 0):    # c has default value
	print(a, b, c)
myfunc(b = 2, a = 4)       		# using name of parameter

# variable length argument, non keyword(*) and keyword(**)
def myfunc(*args, **kargs):
	print(args)				
	print(kargs)
myfunc(1,2,3,4,a=3,b=8)

# scope of variable
# global and local scope
x = 10					# global
def myfunc():
	x = 5								# local
	print(x)						# 5
myfunc()
print(x)							# 10

# modules in python
# import keyword to import a module
import demo 		# contains mydemo function
print(demo.mydemo("Hello"))

# Operators in python
# - Arithmatic Operators	(+,-,*,/,%,//,**)
print("2 + 4 is", 2 + 4)
print("3 - 4 is", 3 - 4)
print("8 * 4 is", 8 * 4)
print("2 / 2 is", 2 / 2)
print("10 % 3 is", 10 % 3)
print("50 // 10 is", 50 // 10)
print("2 ** 3 is", 2 ** 3)

# - Comparison Operator		(<,>,<=,>=,==,!=)
print("2 < 4 is", 2 < 4)
print("3 > 4 is", 3 > 4)
print("8 <= 4 is", 8 <= 4)
print("2 >= 0 is", 2 >= 0)
print("1 == 0 is", 1 == 0)
print("5 != 10 is", 5 != 10)

# - Logical Operator			(and, or, not)
a = 2
b = 6
c = 9
if a >= b and a >= c:
	print(a)
elif b >= a and b >= c:
	print(b)
else:
	print(c)

# - Assignment Operator		(=, +=, -+, *=, /=, //=, **=, %=)
count = 0
for i in range(10):
	count += 1						
print(count)					# 10

# - Membership Operator		(in, not in)
print(1 in [1,2,3,4])			# True
print(5 not in [1,2,3,4])	# True

# - Identity Operator			(is, is not)
print(10 is 10)				# True
print(10 is not 10)		# False
