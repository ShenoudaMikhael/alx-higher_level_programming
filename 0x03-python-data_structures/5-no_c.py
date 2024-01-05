#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        new_string += i if i != "c" and i != "C" else ""
    return new_string
