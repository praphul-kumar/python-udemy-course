# Understanding Cinditionals in Python

"""
    - Conditional statements in Python play a key role in determining the direction of program execution. 
    - Among these, If-Else statements are fundamental, 
        - providing a way to execute different blocks of code based on specific conditions. 
        - As the name suggests, If-Else statements offer two paths, 
        - allowing for different outcomes depending on the condition evaluated.
"""

# syntax

"""
    if condition:
        statement executes if the condition is true
    else:
        statements executes when the condition is false
"""

is_old = False
is_licenced = False

if is_old:
    print('You are old enough to drive!')
elif is_licenced:
    print('You have a licence to drive!')
else:
    print('you are not allowed to drive!')