# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: May 13, 2025
# Calculator that accepts the operation as well
# Uses a function and returns the result fo the operation
# It ask for three parameters in main


# Define the calculations function, for three parameters
def calculate(operator, first_number, second_number):

    # operation for all the operators (+, -, /, *, %)
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    elif operator == "%":
        return first_number % second_number


# Define main function
def main():
    # Get the operator from the user as a string
    operator = input("Enter the operator you want to use (+, -, /. *, %): ")

    # If not statement if the operator from the user is an invalid input
    if (
        operator != "+"
        and operator != "-"
        and operator != "*"
        and operator != "/"
        and operator != "%"
    ):
        print("Invalid operator")
        # return for stopping the program if it is an invalid operator
        return

    # Get user first number
    first_number_str = input("Enter the first number: ")
    # Try catch for first num, type cast string to float
    try:
        first_number = float(first_number_str)
    except Exception:
        print("Invalid first number")
        return

    # Get user input second number as string
    second_number_str = input("Enter the second number: ")

    # Try catch for second num, type casting string to float
    try:
        second_number = float(second_number_str)
    except Exception:
        print("Invalid first number")
        return

    # call the calculate function in a variable
    result = calculate(operator, first_number, second_number)

    # Display the calculations
    print(f"{first_number} {operator} {second_number} = {result :.2f}")


if __name__ == "__main__":
    main()
