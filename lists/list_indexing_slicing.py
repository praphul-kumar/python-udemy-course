# Understanding Indexing and slicing in List 

grocery_cart = ["Banana", "Musterd Oil", "Palm Oil", "OREO", "Notebooks", "Pens"]

print(grocery_cart)

# Accessing item of list using index value

print(grocery_cart[1]) # Musterd Oil
print(grocery_cart[3]) # OREO

# Slicing in List

# Slicing works same as string on list too
# [start:stop:stepover]

print(grocery_cart[1:5]) # ['Musterd Oil', 'Palm Oil', 'OREO', 'Notebooks']

print(grocery_cart[1:]) # ["Banana", "Musterd Oil", "Palm Oil", "OREO", "Notebooks", "Pens"]

print(grocery_cart[:5]) # ['Musterd Oil', 'Palm Oil', 'OREO', 'Notebooks']
