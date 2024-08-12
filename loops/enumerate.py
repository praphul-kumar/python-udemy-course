"""
    The enumerate () function adds a counter to an iterable and 
    returns it in the form of an enumerating object. 
    This enumerated object can then be used directly for loops 
    or converted into a list of tuples using the list() function.
"""

"""
    Syntax: enumerate(iterable, start)
"""

for index, char in enumerate('Hi'):
    print(index, char)
    
for i, item in enumerate([1, 2, 3]):
    print(i, item)
    
# get the Index of value 50
for i, v in enumerate(range(100)):
    if v == 50:
        print(i)
        
    