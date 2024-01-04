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

    @width.setter
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

    @height.setter
    def height(self, value):
        """ll"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """per"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
