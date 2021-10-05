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

# RESOURCES TO LEARN MORE ON PYTHON VARIABLES
# https://realpython.com/python-variables/
# 
