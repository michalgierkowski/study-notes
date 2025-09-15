# dictionary = a collection of {key:value} pairs
#              ordered and changeable. no duplicates

# .keys() --> grabs just the keys (England)]
# .values() --> grabs just the value (London)
# .items() --> both, key and value (pair)


capitals = {"England":"London",
            "USA": "Washington DC",
            "China": "Beijing",
            "Russia": "Moscow",}


#print(dir(capitals)) shows different methods for dictionaries / replace help with dir 

# print(capitals.get("Russia")) # gets the value of the key "USA", if entered a Key with no value` --> prints "None"



# ask_input = input("Enter a capital >  ")
# if ask_input in capitals:           # if users input does not exist in dictionary
    # print("That capital does exist")
# else:                               # this checks if key is in dictionary
    # print("That capital does not exist")


# capitals.update({"Germany":"Berlin"}) # adds a new key/value pair to dictionary
# capitals.update({"England":"Leeds"}) # or change existing value

# capitals.pop("China") # removes key along with it's value 
# if no key found --> error
# capitals.popitem() removes recent key added to dic
# capitals.clear() clears dic


# info = capitals.items()

# for country, value in info: gives first string as country, second string as value
    # print(f"{country} = {value}")