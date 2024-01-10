#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != type(""):
        return 0
    num = 0
    for i, l in enumerate(roman_string):
        if roman_string[i] == "I":
            num += 1
        elif roman_string[i] == "V":
            num += 5
            if i != 0 and roman_string[i - 1] == "I":
                num -= 2
        elif roman_string[i] == "L":
            num += 50
            if i != 0 and roman_string[i - 1] == "X":
                num -= 20
        elif roman_string[i] == "D":
            num += 500
            if i != 0 and roman_string[i - 1] == "C":
                num -= 200
        elif roman_string[i] == "X":
            num += 10
            if i != 0 and roman_string[i - 1] == "I":
                num -= 2
        elif roman_string[i] == "C":
            num += 100
            if i != 0 and roman_string[i - 1] == "X":
                num -= 20
        elif roman_string[i] == "M":
            num += 1000
            if i != 0 and roman_string[i - 1] == "C":
                num -= 200
    return num
