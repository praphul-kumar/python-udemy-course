
# -------------- Copy list using slice -------------

amazon_cart = [
    'notebooks',
    'sungalsses',
    'toys',
    'grapes'
]

"""
    Here, if we try to copy amazon_cart into new variable using noraml assignment operator
    - then the new variable will also be pointing to the same reference 
    - so, when we will modify any of them it will affect both lists
    - for Example:-
"""

new_cart = amazon_cart

print(amazon_cart) # ['notebooks', 'sungalsses', 'toys', 'grapes']
print(new_cart) # ['notebooks', 'sungalsses', 'toys', 'grapes']

# Updating 1st item of new_cart

new_cart[0] = 'laptop'

print(new_cart) # ['laptop', 'sungalsses', 'toys', 'grapes']
print(amazon_cart) # ['laptop', 'sungalsses', 'toys', 'grapes']

"""
    Here, you can clearly see that updating one list caused both lists to be updated.

    so, If we want to copy a list without sharing the same reference 
    we can do something like below.
"""

new_cart = amazon_cart[:]

print(new_cart) # ['laptop', 'sungalsses', 'toys', 'grapes']
print(amazon_cart) # ['laptop', 'sungalsses', 'toys', 'grapes']

new_cart[3] = 'Apple'

print(new_cart) # ['laptop', 'sungalsses', 'toys', 'Apple']
print(amazon_cart) # ['laptop', 'sungalsses', 'toys', 'grapes']
