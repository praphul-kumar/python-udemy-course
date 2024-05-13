# Exercise: 
# - Take name and Password as input from user, 
# - then check the length of the password
# - hide the password into '*',
# - print the greeting message

name = input('Enter Name: ')
password = input('Enter Password: ')

password_length = len(password)
secret_password = '*' * password_length

greeting_message = f'Hello {name}, your password \'{secret_password}\' is {password_length} letters long.'

print(greeting_message)