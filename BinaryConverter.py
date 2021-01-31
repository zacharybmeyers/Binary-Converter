# Author:       Zachary Meyers
# Date:         2021-01-29
# Description:  Provides a simple conversion from unsigned binary to decimal,
#               tests for valid input with try/except, loops until the user wants to quit

from BinaryFunctions import binary_to_decimal


class OutOfRangeError(Exception):
    pass


def is_binary(a_string):
    """Checks whether the user's string is valid binary"""
    for char in a_string:
        if char != "0" and char != "1":
            raise OutOfRangeError
        else:
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
            if is_binary(usr_input):
                print("Decimal: {}".format(binary_to_decimal(usr_input)))
        # raise exception for invalid input
        except OutOfRangeError:
            print("That value is not in binary!")
    print("See ya!")


if __name__ == "__main__":
    main()
