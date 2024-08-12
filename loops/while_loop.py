"""
    While Loop
"""

"""
    Syntax:
        while condition:
            body
"""

# it will iterate over and over untli the condition will be false
i = 0
while i < 5:
    print(i)
    i += 1

# While with else block
# it will execute the else block once the condition will turm false
i = 0
while i < 3:
    print(i)
    i += 1
else: 
    print('Done with all the work!')
    
# it is very importent when we don't know how many times the loop will iterate like below

while True:
    response = input('Say something: ')
    if (response == 'bye'):
        break