# Author:       Zachary Meyers
# Date:         01/29/2021
# Description:  Provides a simple conversion from unsigned binary to decimal,
#               tests for valid input with try/except, loops until the user wants to quit

from binary_functions import binary_to_decimal


class OutOfRangeError(Exception):
    pass


def binary_check(a_string):
    """Checks whether the user's string is valid binary"""
    for char in a_string:
        if char == "0" or char == "1":
            continue
        else:
            raise OutOfRangeError
    return True


def main():
    # greet user
    print("Hello! Welcome to the unsigned binary converter.\n"
          "Type 'quit' to exit.")

    # loop until user wants to quit
    while True:
        usr_input = input("Unsigned binary: ")
        # exit loop
        if usr_input == "quit":
            break
        # compute and print decimal conversion
        try:
            if binary_check(usr_input) is True:
                print("Decimal: {}".format(binary_to_decimal(usr_input)))
        # raise exception for invalid input
        except OutOfRangeError:
            print("That value is not in binary!")
    print("See ya!")


if __name__ == "__main__":
    main()
