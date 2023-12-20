#!/usr/bin/python3
""" this module defines a empty class square """


class Square:
    """ empty class for task 0 """
    def __init__(self, size=0):
        """ Initialize class """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
             self.__size = size
