#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


def write_file(filename="", text=""):
    """
        read_file reads teaxt file and prints to stdout
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
