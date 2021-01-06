import binary_converter

usr_binary = input("Hello! Welcome to the binary converter. \n"
                   "Please enter your binary number: ")


def valid_binary(a_string):
    """Returns true if a given string is in binary"""
    valid = True
    for char in a_string:
        if char != "0" and char != "1":
            valid = False
    return valid


if valid_binary(usr_binary) is True:
    print("Decimal: {}".format(binary_converter.binary_to_decimal(usr_binary)))
else:
    print("Invalid input.")
