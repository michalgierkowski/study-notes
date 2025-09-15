# Logical operators = allows to evaluate multiple conditions (or, and, not)
#     Can be linked together


#     or = at least one condition must be True for the entire statement to be true

temp = 25
is_raining = False  # boolean = True means Yes | False means No

if temp > 25 or temp < 0 or is_raining:  # if one of these conditions is True 
    print("The outdoor event is cancelled!")  # prints as result
else:     # if conditions is false
    print("The outdoor event is still scheduled!") # prints as result

#     and = both conditions must be True for the entire statement to be true

temp = 24
is_sunny = True

if temp >= 28 and is_sunny:   # both of these conditions must be True for this to be executed
    print("It is HOT outside.") # then prints this
    print("It is also SUNNY")

elif temp <= 0 and is_sunny:  # both conditions are true | if temp less than but equal to 0
    print("It is COLD outside.") 
    print("But it's also SUNNY") # which means this will be executed 

elif temp < 28 and temp > 0 and is_sunny: # both conditions are true here aswell
    print("It is WARM outside.") 
    print("And it's also SUNNY")


# not = inverts the condition (checks if it's not False or not True) is a logical operator that simply flips True to False and False to True.

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:   
    print("It is HOT outside.")
    print("It is also SUNNY")

elif temp <= 0 and is_sunny:  
    print("It is COLD outside.") 
    print("But it's also SUNNY") 

elif temp < 28 and temp > 0 and is_sunny: 
    print("It is WARM outside.") 
    print("And it's also SUNNY")

elif temp >= 28 and not is_sunny: # if it's NOT sunny (does the opposite what your looking for)
    print("It is HOT outside.")
    print("It is also CLOUDY") # prints this as result

elif temp <= 0 and not is_sunny:  
    print("It is COLD outside.") 
    print("But it's also CLOUDY") # same here

elif temp < 28 and temp > 0 and not is_sunny: 
    print("It is WARM outside.") 
    print("And it's also CLOUDY") 