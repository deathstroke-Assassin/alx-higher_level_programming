#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


import json


def from_json_string(my_str):
    """
        read_file reads teaxt file and prints to stdout
    """
    return json.loads(my_str)
