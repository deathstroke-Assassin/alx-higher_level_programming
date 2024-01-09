#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


import json


    def save_to_json_file(my_obj, filename):
    """
        read_file reads teaxt file and prints to stdout
    """
    with open(filename, "w") as j:
        json.dump(my_obj, j)
