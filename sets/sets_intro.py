# Introductions to Set in Python

"""
    Set:
        - Sets are used to store multiple items in a single variable.

        - Set is one of 4 built-in data types in Python used to store collections of data, 
            the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

        - A set is a collection which is unordered, unchangeable*, and unindexed.

        - set does not allow duplicates value
"""

my_set = {1, 2, 3, 4, 5, 5}

print(my_set) # {1, 2, 3, 4, 5}

# Converting a list to set
my_list = [1, 2, 3, 4, 5, 6, 7]
my_set = set(my_list)
print(my_set) # {1, 2, 3, 4, 5, 6, 7}

# Converting Set to list
my_list = list(my_set)
print(my_list) # [1, 2, 3, 4, 5, 6, 7]
