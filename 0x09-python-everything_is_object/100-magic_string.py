#!/usr/bin/python3
def magic_string():
    magic_string.icount = getattr(magic_string, "icount", 0) + 1
    return "BestSchool, " * (magic_string.icount - 1) + "BestSchool"
