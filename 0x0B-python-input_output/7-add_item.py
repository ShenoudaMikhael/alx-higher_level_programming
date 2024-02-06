#!/usr/bin/python3
"""Add Item to Json file Module"""
import sys
import os

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


if __name__ == "__main__":
    arg_list = sys.argv[1:]
    my_list = []
    if os.path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
        my_list.extend(arg_list)
        save_to_json_file(my_list, "add_item.json")
    else:
        my_list.extend(arg_list)
        save_to_json_file(my_list, "add_item.json")
