import modul_system_cal


def test_uncode():
    print("The test of changing base of number from X to 10")
    print(f"Base 2 right answer {int('101010', 2)}: ", modul_system_cal.uncode_system_calculator("2","101010"))
    print(f"Base 4 right answer {int('302023', 4)}: ", modul_system_cal.uncode_system_calculator("4","302023"))
    print(f"Base 8 right answer {int('125', 8)}: ", modul_system_cal.uncode_system_calculator("8","125"))
    print(f"Base 16 right answer {int('FF', 16)}: ", modul_system_cal.uncode_system_calculator("16",'ff'))


def test_cange_base():
    print("The test of changing base of number from 10 to X")
    print(f"Base 8 right answer {oct(42)[2:]}: ", modul_system_cal.system_calculator("8", "42"))
    print(f"Base 16 right answer {hex(255)[2:]}: ", modul_system_cal.system_calculator("16", "255"))
    print(f"Base 16 right answer {hex(753)[2:]}: ", modul_system_cal.system_calculator("16", "753"))
    print(f"Base 2 right answer {bin(10)[2:]}: ", modul_system_cal.system_calculator("2", "10"))
    print(f"Base 8 right answer {oct(125)[2:]}: ", modul_system_cal.system_calculator("8", "125"))
    print("Base 4 right answer 302023: ", modul_system_cal.system_calculator("4", "3211"))


if __name__ == '__main__':
    test_uncode()
    print()
    test_cange_base()
