# --------------------------------------
# TITLE:    Week 3 - Variable Naming and Style Guide
# AUTHOR:   Clint MacDonald
# DATE:     Jan 21, 2025
# PURPOSE:  To demonstrate the basic variable names, style guide, 
#           and entering formulas
# --------------------------------------

# Variables are used to store data in a program.
#      The name of variable is a reference to a memory location
# 
# appropriate variable names:

# student's first name
student_first_name = "John" # GOOD - descriptive, uses snake_case
first_name = "John"         # DECENT - descriptive, but not specific
f_name = "John"             # UNACCEPTABLE - abbreviation is not clear
fName = "John"              # UNACCEPTABLE - abbreviation not used
studentFirst = "John"       # DECENT - camel case is used but not descriptive
student_fname = "John"      # UNACCEPTABLE - abbreviate
student_name = "John"       # BAD - not specific enough, assumption, sorting?
StudentFirstName = "John"   # Unacceptable - PascalCase is not for variables
studentFirstName = "John"   # Good - camelCase is used, descriptive
studentfirstname = "John"   # BAD - no separation between words

std_first_name = "John"     # BAD - abbreviation is not clear
Student_First_Name = "John" # BAD - PascalCase and snake is not for variables

# --------------------------------------
# Different Cases
# --------------------------------------
# snake_case - all lowercase with underscores between words
# camelCase - first word is lowercase, subsequent words are capitalized
# PascalCase - all words are capitalized
# UPPER CASE - all capitals
# lower case = all lower case letters


# abbreviations
rcm = "Royal Conservatory of Music"
rcm = "Robert Clint MacDonald"

# variables - CamelCase OR snake_case, 
#           - descriptive in nature, 
#           - not contain abbreviations
#           - not make assumptions

# your Mom's Birthday
mother_birthday = "May 5, 1960" 
motherBirthday = "May 5, 1960"

# your favourite colour
favourite_colour = "blue"
favorite_color = "blue"
favouriteColour = "blue"
favoriteColor = "blue"
favoriteColour = "blue" # BAD - mixed cultural spellings

# the value of the mathematical term pi
pi = 3.14159    # unacceptable 
PI = 3.14159    # GOOD - Constants are written in all caps
Pi = 3.14159    # unacceptable
PIE = 3.14159   # BAD - misspelled

# the speed of light
SPEED_OF_LIGHT = 299792458  #acceptable
speed_of_light = 299792458  # bad
lightSpeed = 299792458      # bad
speedOfLight = 299792458    # bad
c = 299792458               # decent but still bad
C = 299792458               #acceptable

# the number of days in a week
# context specific
NUMBER_OF_DAYS_IN_WEEK = 7  #acceptable
days_in_week = 5            #acceptable

# --------------------------------------
# entering formulas in software
# --------------------------------------

# formula for C to F conversion
C = 24
F = C * 9 / 5 + 32
F = 9 / 5 * C + 32
F = (9 / 5) * C + 32    
F = 9 / (5 * C) + 32  # wrong

# pythagorean theorem
a = 5
b = 12
c = (a ** 2 + b ** 2) ** 0.5
#c = (math.sqrt(math.pow(a, 2) + math.pow(b, 2))) 


# --------------------------------------
# characters in a string
# --------------------------------------

print("--------------------")
# a string is a sequence of characters (array)
# each character has a position in the string, starting at 0

professors_name = "Clint MacDonald"
print(professors_name[0]) # C
print(professors_name[1]) # l
print(professors_name[9]) # D

# extracting from the end
print(professors_name[-1]) # d
print(professors_name[-5]) # o

# slicing   
print(professors_name[0:5]) # Clint  - first five letters
    # first number is inclusive, second number is exclusive
print(professors_name[3:7]) # nt M  - 4th to 7th letter

# everything but the last character
print(professors_name[:-1]) # Clint MacDonal
print(professors_name[:-4]) # Clint MacDo

print("--------------------")
