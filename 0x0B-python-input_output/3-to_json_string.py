#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


import json


def to_json_string(my_obj):
    """
        read_file reads teaxt file and prints to stdout
    """
    return json.dumps(my_obj)
