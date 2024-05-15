# Exploring some methods of Set

my_set = {1, 2, 3, 4, 5, 6, 7}

# len(): returns the length of a set
print(len(my_set)) # 7

# add(): add an item to the set
my_set.add(8)
print(my_set) # {1, 2, 3, 4, 5, 6, 7, 8}

my_set.add(9)
print(my_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# copy(): returns a copy of the set
new_set = my_set.copy()
print(new_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# pop(): removes an element from the set
new_set.pop()
print(new_set) # {2, 3, 4, 5, 6, 7, 8, 9}

# remove(): removes the specified element
new_set.remove(9)
print(new_set) # {2, 3, 4, 5, 6, 7, 8}

# clear(): removes all items of the set
new_set.clear()
print(new_set) # set()

my_set = {1, 2, 3, 5, 6}
your_set = {4, 5, 6, 7, 8, 9, 10}

# discard(): removes the specified item
my_set.discard(5)
print(my_set) # {1, 2, 3, 6}

# difference(): returns a set containing the difference between two or more sets
print(my_set.difference(your_set)) # {1, 2, 3}

# difference_update(): removes the items in this set that are also included in another, specified set
my_set.difference_update(your_set)
print(my_set) # {1, 2, 3}

# intersection(): Returns a set, that is the intersection of two other sets
my_set = {1, 2, 3, 5, 6}
print(my_set.intersection(your_set)) # {5, 6}

# shorthand for intersection in python
my_set = {1, 2, 3, 5, 6}
print(my_set & your_set) # {5, 6}


# intersection_update(): Removes the items int his set that are not present in other, specified set(s)
my_set.intersection_update(your_set)
print(my_set) # {5, 6}

# union(): Return a set containing the union of sets
print(my_set.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Shorthand for union in Python
print(my_set | your_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# isdisjoint(): Returns whether two sets have a intersection or not
my_set = {1, 2, 3}
print(my_set.isdisjoint(your_set)) # True

my_set = {1, 2, 3, 4, 5, 6}
print(my_set.isdisjoint(your_set)) # False


my_set = {4, 5}
your_set = {4, 5, 6, 7, 8}

# issubset(): Returns whether another set contains this set or not
print(my_set.issubset(your_set)) # True
print(your_set.issubset(my_set)) # False

# issuperset(): returns whether this set contains another set or not
print(my_set.issuperset(your_set)) # False
print(your_set.issuperset(my_set)) # True

# symmetric_difference(): returns a set with the symmetric differences of two sets

# symmetric_difference_update(): inserts the symmetric differences from this set and another

# update(): Update the set with the union of this set and others