# Learning about some methods of list class

basket = [9, 1, 2, 3, 4, 5, 6, 7, 8]

# len() : returns the length of the list
print(len(basket)) # 9

# append() : Adds an element to the end of the list
basket.append(9)
print(basket) # [9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert() : Adds an element at the specified position
basket.insert(0, 0)
print(basket) # [0, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# extend() : add the elements of a list to the end of the current list
new_basket = [10, 11, 12]
basket.extend(new_basket)
print(basket) # [9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# copy() : Returns a copy of the list
new_basket = basket.copy()
print(new_basket) # [9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# pop() : Removes the element at the specified position and returns the poped value
basket.pop()
print(basket) # [0, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

basket.pop(12)
print(basket) # [0, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# remove() : Removes the first igem with the specified value
basket.remove(9)
print(basket) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# count() : Returns the number of elemeents with the specified value
print(basket.count(9)) # 2

# index() : returns the index of the first element with the specified value
print(basket.index(9)) # 0

print(basket.index(9, 2)) # 9

# sort() : Sorts the list
new_basket = [2, 1, 9, 0, 8]
new_basket.sort()
print(new_basket) # [0, 1, 2, 8, 9]

# reverse() : Reverse the order of the list index wise(not value wise)
new_basket.reverse()
print(new_basket) # [9, 8, 2, 1, 0]

# clear() : Removes all elements from the list
new_basket.clear()
print(new_basket) # []