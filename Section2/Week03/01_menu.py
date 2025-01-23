# --------------------------------------
# TITLE:    Week 3 - Menu System with Data Validation
# AUTHOR:   Clint MacDonald
# DATE:     Jan 21, 2025
# PURPOSE:  repeating the previous menu with data validation
# --------------------------------------

# greet the user and display the menu
print(
    """
    --------------------------------------
    Welcome to the Menu System
    --------------------------------------
    1. Hello World
    2. Goodbye World
    3. Temperature Conversion
    4. Exit
    """
)

# get the user's input and store it in a variable
main_menu_choice = input("Enter your choice (1 - 4): ")

# check if the user's input is a numeric value
if main_menu_choice.isdigit():
    # convert the user's input to an integer
    choice = int(main_menu_choice[0])

    # check if the number is in the range of the menu
    if choice >= 1 and choice <= 4:
    #if 1 <= choice <= 4:

        # if the number is in the range, process choice
        if choice == 1:
            print("Hello World")
        elif choice == 2:
            print("Goodbye World")
        elif choice == 3:
            print("Temperature Conversion")





        elif choice == 4:
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. You entered a value outside of 1 and 4.")
            exit()

        # if the number is not in the range, give message to user and end program

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        exit()

# if not numeric, then give message to user and end program
else:
    print("Invalid input. Please enter a number.")
    exit()


