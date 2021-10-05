# <variable name> = <value>

# A Python variable is a reserved memory location to store values. In other words,
# a variable in a python program gives data to the computer for processing.
# Every value in Python has a datatype.
# Different data types in Python are Numbers, List, Tuple, Strings, Dictionary, etc.


# Variable assignment works from left to right. So the following will give you syntax error

# Rules for variable naming
# 1. Variable names must start with letter or underscore
# 2. The remainder of your variable name may consist of letters, numbers and underscore
# 3. Names are case sensitive
# 4. No keywords: keywords are preserve words in python
#   e.g ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class'....] ans so on.


full_name = "Young Nnenna"
# full_name is variable name and "Young Nnenna" is the value assigned to the variable name
print(full_name)

double_quote = "John"
single_quote = 'John'
# double quote is the same as single quote

# Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a, they are 2 different variables

# Variable Types in Python
# In many programming languages, variables are statically typed.
# That means a variable is initially declared to have a specific data type,
# and any value assigned to it during its lifetime must always have that type.
# Variables in Python are not subject to this restriction. In Python,
# a variable may be assigned a value of one type and then later re-assigned a value of a different type:

age = 23
age = '23'

# In this case above age has been resigned to string value '23'

result = '5' * 10
print(result)
# prints 5 in 10 times

# Object Identity
# Once an object is created a unique Id is assigned to it, this unique id will not be assigned to another object.
# Once an object’s reference count drops to zero and it is garbage collected,
# and the unique id is made available and may be used again.

# The built-in Python function id() returns an object’s integer identifier.
# Using the id() function, you can verify that two variables indeed point to the same object:

n = 300
m = n
print(id(n))
print(id(m))
# the 2 print above will print the same value, because both n and m is referencing to the same object

m = 400
print(id(m))
# the value changes since m has been reassigned to another object.

print("================")
b = 389
c = 389
print(id(b))
print(id(c))

# You might be thinking that 2 different object is created and hence they should have 2 different Ids but
# Here, b and c are separately assigned to integer objects having value 400.
# But in this case, id(b) and id(c) are identical!
# For purposes of optimization, the interpreter creates objects for the integers
# and its smart enough to know the values that has been create before
# and then reuses them during program execution. Thus, when you assign separate
# variables to an integer value that is already created, they will actually reference the same object.

# RESOURCES TO LEARN MORE ON PYTHON VARIABLES
# https://realpython.com/python-variables/
# https://www.guru99.com/variables-in-python.html

