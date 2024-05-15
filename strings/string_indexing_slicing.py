# Understanding Indexing of Strings in Python
str_1 = "0123456789"
       # 0123456789

"""
    In Python you string can be treated as list 
    - so you can use indexing to get characters or substring from a string using indexing & slicing
"""

print(str_1[0]) # 0
print(str_1[5]) # 5

# Using Slicing on string

# [start:stop:stepover]
print(str_1[0:2]) # 01
print(str_1[1:10]) # 0123456789

# by default stepover is set to 1, 
# but when we change it it will take a step of given number

print(str_1[0:10:2]) # 02468
print(str_1[0:10:3]) # 0369

# If we only pass 'start' then it will start at given index 
# and go all the way to the last index

print(str_1[0:]) # 01234567789

# If we only pass 'stop' then it will start at 0th index 
# and go all the way to the given stop index

print(str_1[:6]) # 012345

# If we only pass 'stepover' then it will start at 0th index 
# and go all the way to the last index by stepping over by given number

print(str_1[::2]) # 02468

# ---------- Negatve Indexing --------------

str_1 = "0123456789"
#        0123456789
#                -1

# In Python, if we pass negative index,
# then it will traverse the string in backwards direction

print(str_1[-1]) # 9
print(str_1[-10]) # 0

# Stepping over in backward direction
print(str_1[::-1]) # 9876543210