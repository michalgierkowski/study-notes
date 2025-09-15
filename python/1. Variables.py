# A Variable = A container for a value this includes = (string, integer, float, boolean)
#              A variable behaves as if it was the value it contains

# Strings = series of characters
first_name = "Rehen" # the variable "first_name" behaves as if it was the value (Rehen)
food = "Chicken"
email = "Fakerisgoat@gmail.com"

print(first_name) # prints out the variable value
print(f"Hello {first_name}") # you can use f-strings = format to make strings which include variables
print(f"You like {food}")
print(f"Your email is {email}")

# Integers = whole numbers
age = 25  # this a integer, with "" it becomes a string
quantity = 3
num_of_students = 30

print(f"You're {age} years old!") # can do same with f-strings
print(f"You're buying {quantity} items!")
print(f"Your class has {num_of_students} of students")

# Float = number with decimal portion 
price = 10.99
distance = 5.6

print(f"The price is £{price}!")
print(f"You ran {distance}km!")

# Boolean = True or False

is_student = True # if you are a student then this is true otherwise it would be False
print(f"Are you a student?: {is_student}")

#Booleans are usually work with if statements

is_student = True
if is_student:     # if this variable is true
    print("You are a student") # then prints the following
else:   # if variable is false
    print("You are NOT a student") # then prints the following

for_sale = True
if for_sale:   # if variable true
    print("That item is for sale")
Else:   # if it's false
    print("That item is NOT available") 