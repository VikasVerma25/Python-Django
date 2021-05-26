# Comment in python
''' Multiline comment
with single quotes '''
""" Multiline comment
with double quotes """

# variable is a name of reserved memory location to store data
# variables in python don't need to be declared as python is dynamically typed
i = 10
print(type(i))							# <class 'int'>
i = 'A'
print(type(i))							# <class 'str'>
print(i)
# assigning value to multiple variables
a , b = 101 , "Akash sir" 
# same value to multiple variables
a = b = c = 0

# Data types in Python.
'''
1. Number
2. String
3. List
4. Tuple
5. Dictionary
6. Boolean
'''
# Number
n = 25
print(type(n))  						# <class 'int'>
print(isinstance(n , int)) 	#	True, it checks if object belongs to a particular class

# String
s = "Hello"
print(s[0]) 								# print character at index 0
print(s[1:4:1])							# ell , slicing [Start:End:Step] - end is not included in result

# List
mylist = [1,2,3,'a',1.5]
print(mylist[:4])						# [1,2,3,'a']
n = int(input("Enter number of elements"))
for i in range(n):
	mylist.append(input())
	
# Tuple
mytuple = (0,15,4,2) 				# similar to list but immutable

# Set
myset = {0,3,5,1}						# set is unordered and no duplicate elements

# Dictionary
# Key-value pairs, unordered and no duplicate keys
mydict = {1:'a', 2:'b', 3:'c'}
print(mydict[2])   					# b
k, v = input("Enter key and value: ").split()
mydict.update({k: v})

