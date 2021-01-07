# Author:       Zachary Meyers
# Date:         01/06/2021
# Description:  Functions that convert binary to other bases

def binary_to_decimal(binary_str):
    """Converts a binary string to a base 10 decimal number"""
    index = len(binary_str) - 1
    decimal = 0
    for bit in binary_str:
        if int(bit) == 1:
            decimal += 2**index
        index -= 1

    return decimal


def main():
    print(binary_to_decimal("00000011"))


if __name__ == '__main__':
    main()