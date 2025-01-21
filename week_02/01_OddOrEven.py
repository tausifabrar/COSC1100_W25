# --------------------
# Title:    Week 2 - Odd or Even
# Author:   Khondokar Tausif Abrar, 100999061
# Date:     January 14, 2025
# Purpose:  A quick program to allow a user input value and determine 
#           if its odd or even
#---------------------

# Greet The User 

print("----------------------------------")
print("Welcome to the Odd or Even program")

# Ask the user for a input, which should be a number and store it in a variable

usrStr = input("Please enter a whole number: ")

# Make sure what the user entered is a number 

if usrStr.isnumeric():
    usrInt = int(usrStr)

    # Determine if the number is odd or even

    if usrInt % 2 == 0 :
        result = "even"
    else:
        result = "odd"

# Display the result to the user
    print("The number %i is %s" % (usrInt, result))
else:
    print("You did not enter a whole number, could not compute!")
