def print_system_calculator(sys, input):
    """
    Converts a number from base 10 to another base specified by sys.

    :param sys: The base to convert the number to.
    :param input: The number to convert.
    :return: The converted number as a string.
    """
    try:
        base = int(sys)
        num = int(input)
        if base < 2:
            return "Unsupported system. Please use base 2 or higher."
        if num < 0:
            return "Unsupported number. Please use non-negative integers."

        symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if base > len(symbols):
            return "Unsupported system. Please use a smaller base."

        digits = []
        while num != 0:
            digits.append(symbols[num % base])
            num //= base

        return "".join(digits[::-1])
    except BaseException as s:
        print("The exception is: ", s)


def uncode_system_calculator(sys, num):
    """
    Converts a number from a specified base to base 10.

    :param sys: The base of the input number.
    :param num: The number to convert.
    :return: The converted number as an integer.
    """
    base = int(sys)
    try:
        if base < 2:
            return "Unsupported system. Please use base 2 or higher."
        if base < 0:
            return "Unsupported number. Please use non-negative integers."
        else:
            str_num = str(num)
            return int(str_num, base)
    except BaseException:
        return int(num, base)


if __name__ == '__main__':
    print("The test of changing base of number from X to 10")
    sys = input("Enter base of system: ")
    num = input("Enter a number for changing base: ")
    print(print_system_calculator(sys, num))

    print("The test of changing base of number from 10 to X")
    base = input("Enter base of system: ")
    num_in = input("Enter a number for changing base: ")
    print(uncode_system_calculator(base, num_in))
