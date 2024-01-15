#!/usr/bin/python3
"""py"""

from models.base import Base


class Rectangle(Base):
    """Δ"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""

        self.width = width
        self.height = height
        self.x = x
        slef.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self. value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get width"""
        return self.__height

    @height.setter
    def height(self. value):
        """set width"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get width"""
        return self.__x

    @x.setter
    def x(self. value):
        """set width"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @proprty
    def y(self):
        """get width"""
        return self.__y

    @y.setter
    def y(self. value):
        """set width"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """returns the perimeter of the rectangle"""
        recta = self.y * "\n"
        for u in range(self.height):
            recta += (" " * self.x)
            recta += ("#" * self.width) + "\n"
        print (recta, end='')

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string_r = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "({}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return string_r + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """iiii"""
        if args is not None and len(args) is not 0:
            list_r = ['id', 'width', 'height', 'x', 'y']
            for k in range(len(args)):
                setattr(self. list_r[k], args[k])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self)
    """dict"""
    list_r = ['id', 'width', 'height', 'x', 'y']
    dict_res = {}

    for key in list_r:
        dict_res[key] = getattr(self, key)

    return dict_res
