# Exploring some of the Dictionary methods

user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20
}

# `in` : returns True or False if a key exists in the dictionary
print('basket' in user) # True
print('Name' in user) # False

# get(key, default): returns the value of the specified key if not exists returns None
print(user.get('age')) # 20
print(user.get('name')) # None


# You can also pass default value, so when the key will not exist in the dict 
# then it will return the default value
print(user.get('name', 'Praphul')) # Praphul


# keys(): Returns a list containing the dictionary's keys

print(user.keys()) # dict_keys(['basket', 'greet', 'age'])


# values(): Returns a list of all the values in the dictionary

print(user.values()) # dict_values([[1, 2, 3], 'Hello', 20])


# items(): Returns a list containing a tuple for each key value pair

print(user.items()) # dict_items([('basket', [1, 2, 3]), ('greet', 'Hello'), ('age', 20)])


# clear() : Removes all the elements from the dictionary
user.clear()
print(user) # {}


# copy() : Returns a copy of the dictionary
user = {
    'name': 'Praphul',
    'designation': 'Software Engineer'
}
user2 = user.copy()
print(user) # {'name': 'Praphul', 'designation': 'Software Engineer'}
print(user2) # {'name': 'Praphul', 'designation': 'Software Engineer'}


# pop(): removes the element with specified key
user2.pop('designation')
print(user2) # {'name': 'Praphul'}


# popitem(): Removes the last inserted key-value pair
print(user2.popitem()) # ('name', 'Praphul')
print(user2) # {}


# update(): Update the dictionary with the specified key-value pair 
user.update({'age': 25})
print(user) # {'name': 'Praphul', 'designation': 'Software Engineer', 'age': 25}