# List Unpacking

list_1 = [1, 2, 3, 4, 5, 6, 7, 8]

# NOTE:- no of variables should be same as the no of items in the list
a, b, c = [1, 2, 3]
print(a) # 1
print(b) # 2
print(c) # 3

# NOTE:- You can also use *variable_name to get rest of the list
a, b, c, *others = list_1
print(a) # 1
print(b) # 2
print(c) # 3
print(others) # [4, 5, 6, 7, 8]

a, b, c, *others, d = list_1
print(a) # 1
print(b) # 2
print(c) # 3
print(others) # [4, 5, 6, 7]
print(d) # 8