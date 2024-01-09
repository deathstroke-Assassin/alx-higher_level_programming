#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


import json


def load_from_json_file(filename):
    """
        read_file reads teaxt file and prints to stdout
    """
    with open(filename, "r") as j:
        return json.load(j)
