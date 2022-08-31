#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    rom_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }

    # roman_string = roman_string.replace("IV", "IIII").replace("IX", "VIIII")
    # roman_string = roman_string.replace("XL", "XXXX").replace("XC", "LXXXX")
    # roman_string = roman_string.replace("CD", "CCCC").replace("CM", "DCCCC")

    num = 0
    _len = len(roman_string)
    for i in range(_len):
        chv = rom_to_int[roman_string[i]]
        if i != _len - 1 and rom_to_int[roman_string[i + 1]] > chv:
            num += rom_to_int[roman_string[i + 1]] - chv
            continue
        num += chv
    return num
