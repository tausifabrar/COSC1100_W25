# --------------------------------------
# TITLE:    Week 2 - Odd or Even
# AUTHOR:   Clint MacDonald
# DATE:     Jan 14, 2025
# PURPOSE:  A quick program to allow a user input value and determine 
#           if it is odd or even
# --------------------------------------

# Greet the User
print("-----------------------------------------------------")
print("Welcome to the Odd or Even program by Clint MacDonald")

# Ask the user for input, which should be a number, and store it in a variable
userStr = input("Please enter a whole number: ")

# make sure what the user entered is a number
if userStr.isnumeric(): 
    # convert the user input to an integer
    userInt = int(userStr)

    # determine if the number is odd or even
    if userInt % 2 == 0:
        result = "even"
    else:
        result = "odd"

    # display the result to the user
    print("The number %i is %s" % (userInt, result))
    
else:
    print("You did not enter a whole number. Could not compute!")

print("-----------------------------------------------------")