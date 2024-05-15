# Immutability in String in Python

"""
    In Python, strings are Immutable 
    - it means that we can not change the value of a string
"""

str_1 = '0123456789'

"""
    Here, if we can try to update the str_1 value at index 1
    - it will throw an type error
    - "'str' object does not support item assignment"
"""

# str_1[1] = '8' # TypeError: 'str' object does not support item assignment

# The Only way you can change a str value, 
# you have to completely reassign the value to the variable

str_1 = '801234567'

print(str_1) # 801234567

str_1 = str_1 + '9'

print(str_1) # 8012345679