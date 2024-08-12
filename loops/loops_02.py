# Running Loops on Dictionary

user = {
    'name': "Golem",
    'age': 4002,
    'can_swim': True
}

for item in user:
    print(item)
    
# Above Loop will iterate over the keys of the dictionary

# To iterate over the items of the dictionary
for item in user.items():
    # It will print (key, value)
    print(item)
    
for key, value in user.items():
    # It will print (key, value)
    print(key, value)
    
# To iterate over the values of the dict
for item in user.values():
    print(item)
    
# To iterate over the keys of the dict
for item in user.keys():
    print(item)