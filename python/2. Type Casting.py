#Typecasting = process of converting a variable from one data type to another
#              etc.     str(), int(), float(), bool() useful when handling user input
name = "Richard Davidson"
age = 57
gpa = 2.5
is_adult = True

print(type(is_adult))  # this gives you the data type of the variable or value

gpa = int(gpa) # converts into a integer

print(gpa) # prints integer

age = float(age) # converts into a float
print(age) # prints float

age = str(age) # converts into string
print(age) # prints string
print(type(age))  # changes integer to string (type(age)) to prove it is a string

name = bool(name) 
print(name)  # if user enters a name = True
             # if user doesn't enter a name = False (you can ask to re-enter)