#!/usr/bin/python3
"""python3"""


class Base:
    """base"""

    __nb_objects = 0

    def  __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
