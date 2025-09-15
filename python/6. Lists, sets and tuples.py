# collection = single "variable" to store multiple values
# lists = [] ordered and changeable. duplicates are okay
# Set = {} unordered and immutable (unchangeable). add/remove. No duplicates
# Tuple = () ordered and unchangeable. Duplicates are okay - way faster



Males = ["Beta","Sigma","Alpha"]


# Lists

# print(Males[0:3]) index operator can be used in collections such as strings


# lists can be iterated in for loops
# for Male in Males:     # Gets all of the words in the loop  
    # for char in Male:  # for each character for each word
        # print(char)    # print them all out one by one

# print(dir(Males)) # shows methods that list can perform - applies for Lists, sets and tuples
# print(help(Males)) # description for each method - applies for Lists, sets and tuples
# print(len(Males)) # shows how many elements within a list - applies for Lists, sets and tuples
# print("Sigma" in Males) # checks if the "element" is within the list, returns true or false - applies for Lists, sets and tuples

# methods for lists

# Males[0] = "Nonchalant" -> Replaces a element within a list to something new 
# Males.append("Thomas Shelby") # append --> adds on a element within the list
# Males.remove("Beta") # remove --> removes a element within the list
# Males.insert(1, "PIZZA") # adds a element to list to assigned position
# Males.sort() sorts a list in alphabetical order
# Males.reverse() reverses the list order
# Males.clear() # clears the list elements
# Males.index("Beta") # returns value of a element position
# Males.count("Beta") # counts and returns how many of element there is in the list

# Set

# prints a collection unordered (not same order like originally)

foods = {"Pizza","Burger","Fish"} # original order
 
# print(foods)  # prints out a non-original order

# cannot use indexing on set because it's unordered --> print(foods[2]) -> error

# foods.add("Banana")   # adds a element within a set
# foods.remove("Pizza") # removes a element within a set
# foods.pop() removes the first element
# foods.clear()  removes the elements



# Same everything for Tuple



