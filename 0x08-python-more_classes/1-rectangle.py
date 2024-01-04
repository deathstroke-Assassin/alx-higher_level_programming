#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle:
    """pass it"""
    def __init__(self, width=0, height=0):
        """init"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """nn"""
        return self.__width

    @width_setter
    def width(self, value):
        """kk"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """x"""
        return self.__height

    @height_setter
    def height(self, value):
        """ll"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
