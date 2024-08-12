"""
    The range() function returns a sequence of numbers, 
    starting from 0 by default, and increments by 1 (by default), 
    and stops before a specified number.
"""

"""
    syntax: range(start, stop, step)
"""

# Will start from 0 and goes to (n -1)
for item in range(5):
    print(item) # 0,1,2,3,4
    
# will start from 11 and go to (n - 1)
for item in range(11, 20):
    print(item) # 11, 12, 13, 14, 15, 16, 17, 18, 19
    

# Will start from 30 and increment by 2 till (n-1)
for item in range (30, 40, 2):
    print(item) # 30, 32, 34, 36, 38


# Will start from 50 and decrement by -1 till (n + 1)
for item in range(50, 40, -1):
    print(item) # 50, 49, 48, 47, 46, 45, 44, 43, 42, 41
