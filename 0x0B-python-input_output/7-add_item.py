#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
        and then save them to a file"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
args = (sys.argv[1:])
for arg in args:
    my_list.append(arg)

filename = 'add_item.json'
save_to_json_file(my_list, filename)
