# Introduction to Tuple

"""
    Tuple:
        - Python Tuple is a collection of objects separated by commas.
        - Tuple is similar to a Python list in terms of indexing, nested objects, and repetition
        - Python tuple is immutable, unlike the Python list which is mutable.
        - Tuple is faster than List
"""

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Getting item from tuple
print(my_tuple[0]) # 0

# Slicing Tuple
print(my_tuple[1:]) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple[0: 5]) # (0, 1, 2, 3, 4)

# Tuple Unpacking
x, y, z = (1, 2, 3)
print(x) # 1
print(y) # 2
print(z) # 3

x, y, z, *others = my_tuple
print(x) # 0
print(y) # 1
print(z) # 2
print(others) # [3, 4, 5, 6, 7, 8, 9]


# ---------- Tuple Methods --------------

# count(): returns the number of times a specified value occurs in a tuple
print(my_tuple.count(5)) # 1

# index(): Serches the tuple for a specified value and returns the position of where it was found
print(my_tuple.index(3)) # 3
print(my_tuple.index(5)) # 5
