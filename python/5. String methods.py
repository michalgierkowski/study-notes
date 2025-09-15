# Types of string methods

#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number:  ")


#result = len(name)    # length function gives us the length of characters in a string
#result = name.find("A") # gives the position of the first occurrence of a character 
#result = name.rfind("A") # "r" means reverse give the position of the last occurrence of a character
#name = name.capitalize() # capitalizes the first letter only
#name = name.upper() # takes all characters in string and makes them in uppercase
#name = name.lower() # takes all characters in string and makes them in lowercase
#result = name.isdigit() # checks if a string contains only digits and returns true or false 
#result = name.isalpha() # checks if a string contains only alphabetical characters and returns true or false
#result = phone_number.count("1") # counts how many of a character there is from users string
#result = phone_number.replace("1", "xd") # replaces one character with another (left ---> you want to change, right ---> what to change it to)

# .strip() → removes spaces from both ends
# .lstrip() → removes spaces from the left side only
# .rstrip() → removes spaces from the right side only




#print(result)
#print(result)

#(help(str)) # shows every string method


# Challenge
# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter a new username:  ")



if len(username) > 12:     # if username characters greater than 12
    print("Your username can't be more than 12 characters!") # result

elif not username.find(" ") == -1:    # if username finds a space
    print("Your username can't contain spaces")       # prints this

elif not username.isalpha():     # if username contains anything other than letters
    print("Your username can't contain digits")  # does this

# not means "opposite"


else: # if all conditions met
    print(f"Welcome {username}!")   # result



