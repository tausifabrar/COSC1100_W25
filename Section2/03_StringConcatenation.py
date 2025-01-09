# --------------------------
# Title:    String Concatenation
# Author:   Clint MacDonald, StudentID
# Date:     Jan 9, 2025
# Purpose:  This program shows 5 different ways to 
#           concatenate strings in Python.
# --------------------------

#define the variables
first_name = "Clint"
last_name = "MacDonald"

full_name = first_name + " " + last_name

# output the full name 5 different ways
print("Hello, my name is " + full_name + ".")
print("Hello, my name is", full_name, ".")
print("Hello, my name is %s." % full_name)
print(f"Hello, my name is {full_name}.")
print("Hello, my name is {}.".format(full_name))