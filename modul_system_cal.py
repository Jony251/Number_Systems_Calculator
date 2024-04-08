def system_calculator(inp_sys: str, inp_text: str) -> str:
    """
    Converts a number from base 10 to another base specified by sys.
    :param inp_sys: String -> The base to convert number to.
    :param inp_text: String -> The number to convert from base 10 to inp_sys.
    :return: Converted number as a string.
    """
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(symbols)
    try:
        base = int(inp_sys)
        num = int(inp_text)
        if base < 2:
            return "Unsupported system. Please use base 2 or higher."
        if num < 0:
            return "Unsupported number. Please use non-negative integers."

        if base > n:
            return "Unsupported system. Please use a smaller base."

        digits = []
        while num != 0:
            digits.append(symbols[num % base])
            num //= base

        return "".join(digits[::-1])
    except TypeError:
        print('Not an integer! TypeError S')
    except ValueError:
        print('Not an integer! ValueError S')
    except BaseException as s:
        print("The exception is: ", s)


def uncode_system_calculator(inp_sys: str, inp_text: str):
    """
    Converts a number from a specified base to base 10.
    :param inp_sys: String -> The base to convert number to.
    :param inp_text: String -> The number to convert.
    :return: The converted number as an integer.
    """
    try:
        base = int(inp_sys)
        if base < 2:
            return "Unsupported system. Please use base 2 or higher."
        if base < 0:
            return "Unsupported number. Please use non-negative integers."
        else:
            return str(int(str(inp_text), base))
    except TypeError:
        print('Not an integer! TypeError')
    except ValueError:
        print('Not an integer! ValueError')
    except BaseException as s:
        print("The exception is: ", s)


if __name__ == '__main__':
    print("The test of changing base of number from X to 10")
    base_in = input("Enter base of system: ")
    num = input("Enter a number for changing base: ")
    print(system_calculator(base_in, num))

    print("The test of changing base of number from 10 to X")
    base = input("Enter base of system: ")
    num_in = input("Enter a number for changing base: ")
    print(uncode_system_calculator(base, num_in))
