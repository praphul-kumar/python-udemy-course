
# ---------- Formatted Strings ------------

name = 'Johnny'
age = 55

# using normal string concatination
print('hi ' + name) # hi Johnny
print('hi ' + name + '. You are ' + str(age) + ' years old.') # hi Johnny. You are 55 years old.

"""
    The problems we face when we want to put some dynamic content in a string
    using string concatination 
    - we have to break the whole string into multiple chunks
    - convert other data types into str
"""

# Using Formatted string feature of python 2 
# It also works in python 3
print('hi {}, You are {} years old'.format(name, age))

# We can also use index for namespaces 
print('hi {1}, You are {0} years old'.format(age, name))

# Using Formatted string feature of python 3
print(f'hi {name}. You are {age} years old')