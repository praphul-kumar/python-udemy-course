# Learning 'str' data type

"""
    A string can ve written in `''` or `" "`
"""

str_1 = "This is a string"
str_2 = 'This is a string 02'
print(str_1)
print(str_2)

# We can also create multi-line string using 3 ''' 

str_3 = '''
WOW
O O
---
'''

print(str_3)

# String Concatination

'''
    Strings will only be concatinated if both the operands are of string type
'''
print("Hello" + " Kumar")

# Type Conversion

a = str(100) # here we are converting int to string
print(type(a)) # <class 'str'>

b = int(a) # Converting str to int
c = type(b)

print(c) # <class 'str'>


