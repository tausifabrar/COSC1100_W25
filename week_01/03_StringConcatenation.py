# --------------------
# Title:     String Concatenation
# Author:    Khondokar Tausif Abrar, 100999061
# Date:      January 9, 2025
# Purpose:   This program shows 6 different ways to 
#            Concatenate strings in Python.
# ---------------------
# Define the variable

first_name = "Tausif"
last_name ="Abrar"

full_name = first_name + " " + last_name

#output the full name in 5 different ways
print("Hello, my name is " + full_name + ".")
print("Hello, my name is", full_name, "." )
print("Hello, my name is %s." % full_name)
print(f"Hello, my name is {full_name}.")
print("Hello, my name is {}.".format(full_name))
