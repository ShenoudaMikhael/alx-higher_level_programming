#!/usr/bin/python3
"""Append after Module"""


def append_after(filename="", search_string="", new_string=""):
    """append after function"""
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
                i += 1
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
