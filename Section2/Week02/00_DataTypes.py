# --------------------------------------
# TITLE:    Week 2 - Data Types
# AUTHOR:   Clint MacDonald
# DATE:     Jan 14, 2025
# PURPOSE:  To demonstrate the basic data types in Python
# --------------------------------------

# --------------------------------------
# Main Data Types in Programming

# String
# A sequence of characters, alphanumeric, symbols, etc.
# 1 character takes 1 byte of memory
# String requires n + 2 bytes of memory, where n is the number of characters in the string

# Decimal
# a number with a decimal point - with LOTS of decimal places
# 16 bytes of memory

# Float - Floating Point Decimal
# A number with a decimal point - with limited decimal places
# 8 bytes of memory

# Integer 
# A whole number, with no decimal point
# 4 Bytes of memory
# maximum number is: 2^31 - 1 = 2,147,483,647

# Boolean 
# True or False, 1 or 0, Yes or No, On or Off
# Used for logical operations
# use 1 bit of memory

# Date
# A date, with a year, month, and day
# They do not exist

# --------------------------------------

# Memory
# 1 bit or a 1-digit binary number
# 1 byte = 8 bits (3-digit binary number)
# 1 kilobyte = 1024 bytes
# 1 megabyte = 1024 kilobytes
# 1 gigabyte = 1024 megabytes


# --------------------------------------

# Variable Declarations
# integers
xi = 2
yi = 6

# floats
xf = 2.1
yf = 6.3

# strings
xs = "2"
ys = "6"

# booleans
xb = True
yb = False

# --------------------------------------
# do some calculations
print (xi + yi)     # addition
print (xf + yf)     # addition
print (xs + ys)     # string concatenation
print (xb + yb)     # boolean operation (+ = OR)

# mixing them
#print (xi + ys)     # integer + string - ERROR
print (xi + int(ys))    # integer + string casted to an integer - OK

#print(xs + yi)      # string + integer - ERROR
print (xs + str(yi))    # string + integer casted to a string - OK

# floats
print (xf + yf)     # addition
print("The answer is: %f" % (xf + yf))  # formatted output
print("The answer is: %.2f" % (xf + yf))  # formatted output to 2 decimal places

print("%.2f" % (7 / 3))
print("%.2f" % (8 / 3)) # rounds

# division
print (7 / 3)       # division
print (7 // 3)      # integer division

# rounding
print(("%.3f" % (7 / 3))) #outputs a string
#print(("%.3f" % (7 / 3)) + 2)

print(round(7 / 3, 3)) #outputs a float
print(round(7 / 3, 3) + 2) #outputs a float

# formatting string with multiple variables
print("The answer is: %i and %d" % (xi, yi))

fname = "Clint"
lname = "MacDonald"
print("My name is %s %s" % (fname, lname))
