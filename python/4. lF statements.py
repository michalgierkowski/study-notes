# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("What is your age?:  "))

if age >= 18:                          # if user age is greater or equal to 18, if this condition is false it skips vica versa for each
    print("You are signed up!")        # prints result

elif age <0: # you can check more than 1 condition, this is else if statement, if this condition is true then it will be excuted vice versa for each
    print("You haven't been born yet!") # prints this result

# elif age >= 100:    # you can use how many elif statements. but the order does matter
   #  print("You are too old to sign up!") 

else:                                  # if NOT 18 or greater
    print("You must be 18+ to signup") # prints this result