# --------------------
# Title:     Week 2 - Data Types
# Author:    Khondokar Tausif Abrar, 100999061
# Date:      January 14, 2025
# Purpose:  To demonstrate the basic data types in Python
#---------------------
# Main data types in programming

# String 
# A sequence of characters, alphanumeric, symbols etc.
# 1 character takes 1 byte of memory, where n is the number of characters in the string

# Decimal
# A number with a decimal point - with LOTs of decimal places
# 16 bytes of memory

# Float - Floating point Decimal
# a number with a decimal point - with limited decimal places
# 8 bytes of memory

# Integer 
# A whole number, with no decimal point   
# 4 bytes of memory
# max number is: 2^31 - 1 = 2,147,483,647

# Boolean
# True or false, 1 or 0, Yes or no, On or off
# Used for logical operations
# Uses 1 bit of memory

# Date
# A date, with a year, month, and day
# They do not exist

#---------------------------

# Memory
# 1 bit or a 1-digit binary number 
# 1 byte = 8 bits (3-digit binary number)
# 1 kilobyte = 1024 bits
# 1 megabyte = 1024 kilobytes

#----------------------------------
# Variable declaration
# Integer

xi = 2
yi = 2

# Floats

xf=2.1
yf=6.3

# Strings

xs='2'
ys='6'

# Booleans

xb= True
yb= False

#----------------------------
# Do some calculations
print( xi + yi ) # addition
print( xf + yf ) # addition
print( xs + ys ) # string concatenation
print( xb + yb ) # boolean operation

# mixing them
# print( xi + ys ) # integer + string - ERROR
print( xi + int(ys) ) # integer + string casted to an integer - OK
# print( xs + yi ) # string + integer - ERROR
print( xs + str(yi) ) # string + integer casted to a string - OK

# floats
print( xf + yf ) # addition
print("the answer is: %f" % (xf + yf )) # formatted output
print("the answer is: %.2f" % (xf + yf )) # formatted output to 2 decimal places

print("%.2f" % ( 7 / 3 )) 
print("%.2f" % ( 8 / 3 )) # rounds 

# division
print ( 7 / 3 ) # division
print ( 7 // 3 ) # integer division

# rounding
print("%.3f" % ( 7 / 3 )) 
# print(("%.3f" % ( 7 / 3 )) + 2) 
print(round( 7 / 3,3 )) # outputs a float
print(round( 7 / 3,3 ) + 2 ) # outputs a float

# formatting string with multiple variables
fname = "Tausif"
lname = "Abrar"
print("The answer is : %s %s" % (fname, lname))

