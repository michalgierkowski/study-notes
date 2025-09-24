# list comprehension --> a shorter way of writing a loop that builds a list (when not needed lots of steps)
# formula --> [ 3.apply_something(what you want in list), 1.for each item in iterable, 2.filter out(if condition) ]
# example --> squares = [i for i in range(10) if i % 2 == 0]


# Practice Problems


# Make a list of squares of numbers from 0 to 10.
# Solution: squares = [i*i for i in range(10)]
# i*i applies to every number in the loop -> multiplies by itself
# loops from 0 - 9


# Make a list of all numbers from 0 to 20 that are divisible by 3, but store them as strings (like "3", "6", "9").
# Solution: divisible_by_3 = [str(a) for a in range(20) if a % 3 == 0]
# for every element in the range (0-19), check which are divisible by 3 and then add to the list but convert it as a string


# You have a list of words: words = ["apple", "banana", "cherry", "date"]
# Make a list of the lengths of these words.
# length_of_words = [len(word) for word in words]
# go through each element, filter out (no condition this time), and add the length of each item to the list


#You need to loop through numbers from 0 to 20.
# If the number is even, add double of it.
# If the number is odd, add triple of it.
# But skip numbers less than 5.

#number_list = []
#for number in range(20):
    #if number < 5:                     checks "skip" condition first    
        #continue
    #elif number % 2 == 0:
        #number_list.append(number * 2)
    #elif number % 2 == 1:
        #number_list.append(number * 3)
# Takeaway:
# Don't use list comprehension as we are dealing with multiple steps (conditions)


#You have a 2D grid:
#x ranges from 0 to 2
#y ranges from 0 to 2
#Make a list of all coordinate pairs [x, y], except when x == y.
#Solution: pairs = [ [x,y] for x in range(3) for y in range(3) if not x == y ]
#Takeaway:
#When dealing with one or more values inside comprehension we need to wrap variables with [list], (tuple) or {set}


#Make a list of all triples [x, y, z] where each of x, y, and z can range from 0 to 1
#Solution: triples = [ [x,y,z] for x in range(2) for y in range(2) for z in range(2)]
#In this case, we are wrapping x,y,z in [list] because we are dealing with 3 values


#Make a list of all triples [x, y, z] where each of x, y, and z can range from 0 to 1, but skip any triple where x + y + z == 1.
#triples = [ [x,y,z] for x in range(2) for y in range(2) for z in range(2) if not x + y + z == 1]
# for each item (x,y,z) go through (0-1) and exlcude any that has a sum of 1