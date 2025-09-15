# conditional expression = One line shortcut for using if-else statement 
#                          We can print or assign one of two values based on a condition
#                          Return X if our condition is true else return Y
#                          Formula = X if condition else Y

num = 5
a = 6
b = 3
age = 17
temperature = 28
user_role = "Admin".lower() # .lower() allows any type of case (upper and lower) in strings


# print("Positive" if num > 0 else "Negative")  # num > 0 (If num is GREATER than 0) prints "Positive" if num is less than 0 prints "Negative"
# max_num = a if a > b else b # return variable a if a is greater than b else return b
# min_num = a if a < b else b # return variable a if a is less than b else return b
# result = "Even" if num % 2 == 0 else "Odd"   If num is even --> prints "Even" else prints "Odd"
# status = "Adult" if age >= 18 else "Child"   If age is greater than or equal to 18 print "Adult" else prints "Child"
# weather = "Hot" if temperature > 20 else "Cold" If temperature is greater than 20 prints "Hot" else prints "Cold"
access = "Access confirmed" if user_role == "admin" else "Unauthorized access" # If user_role equals to "admin" prints "Allowed access" otherwise prints "Unauthorized access"



# print(max_num)
print(access)