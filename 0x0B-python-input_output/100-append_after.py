#!/usr/bin/python3
"""Append after Module"""


def append_after(filename="", search_string="", new_string=""):
    """append after function"""
    if len(search_string) == 0:
        return
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for index, line in enumerate(lines):
            if search_string in line:
                lines.insert(index + 1, new_string)
                index += 1
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
