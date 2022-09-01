#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None:
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

    roman_string = roman_string.replace("IV", "IIII").replace("IX", "VIIII")
    roman_string = roman_string.replace("XL", "XXXX").replace("XC", "LXXXX")
    roman_string = roman_string.replace("CD", "CCCC").replace("CM", "DCCCC")

    num = 0

    for ch in roman_string:
        if not rom_to_int.get(ch):
            return 0
        num += rom_to_int[ch]
    return num
