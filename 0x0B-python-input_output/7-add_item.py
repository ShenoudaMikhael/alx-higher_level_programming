#!/usr/bin/python3
"""Add Item Module"""
import sys
import os

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


a = sys.argv[1:]
l = []
if os.path.exists("add_item.json"):

    l = load_from_json_file("add_item.json")
    l.extend(a)
    save_to_json_file(l, "add_item.json")
else:
    l.extend(a)
    save_to_json_file(l, "add_item.json")
