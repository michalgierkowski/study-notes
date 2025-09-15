# execption = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1,try (code which might cause error), 2.except (What to do if error appears), 3.finally (what to do if error appears)
#             Use only when something MIGHT break

# use if = predictable mistakes, like using digits in alpha only inputs
# use try/except = unpredictable exceptions like missing file, bad type cast (like incorrect type)


# 1 / 0 - ZeroDivisionError, division by 0
# 1 + "1" - TypeError, attempt operation at a value with incorrect data type
# int("Hello") - ValueError, attempt of type casting invalid value


while True:
    try:                                        # code which may cause error   
        number = int(input("Enter a number:  "))
        result = 10 / number
        print(result)
        
        break                                   # if correct value entered, end the
    
    except ValueError:                          # specific errors to look out for and what to do
        print("You did not enter a number.")
    except ZeroDivisionError:
        print("You cannot divide by 0")
    except Exception:
        print("Something went wrong!")          # catches missed Exceptions
    finally:                                     
        print("This line always runs.")         # this will always execute (optional) - usually used in handling with files



# except Exception: catches all errors (not good to use)