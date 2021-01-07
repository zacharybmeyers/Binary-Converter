# Author:       Zachary Meyers
# Date:         01/06/2021
# Description:  Provides a simple conversion from binary to decimal,
#               tests for valid input with try/except

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
    print("Decimal: {}".format(binary_to_decimal(a_string)))


usr_binary = input("Hello! Welcome to the binary converter. \n"
                   "Please enter your binary number: ")


try:
    binary_check(usr_binary)
except OutOfRangeError:
    print("That value is not in binary!")
