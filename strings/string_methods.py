# Learning some built-in functions & methods of str class in python

"""
    Built-in functions:
        - a built-in function have the syntax of 
        - function_name(*arguments)

    Methods:-
        - methods are similar to functions but, they are owned by some class
"""

str_1 = "Helloooooo..."

# len() : returns length of the string
print(len(str_1)) # 13

# ---------- String Methods --------------

quote = "this is a quote"

# str.capitalize() : return a copy of string with its first character capitalized and the rest lowercased
print(quote.capitalize()) # This is a quote

# str.upper() : return a copy of string with its all characters capitalized
print(quote.upper()) # THIS IS A QUOTE

# str.upper() : return a copy of string with its all characters lowercased
print(quote.lower()) # this is a quote

# str.find() : return the index of first occurance of the subtring in a string
print(quote.find('is')) # 2

# str.replace() : return a copy of string with replaced substring 
print(quote.replace('a', 'one')) # this is one quote