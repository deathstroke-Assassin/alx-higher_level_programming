#!/usr/bin/python3
"""
    0-read_file: read_file()
"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            read_file reads teaxt file and prints to stdout
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
            replaces all attributes of the Student Instance.
            Args:
                json (dictionary): reload data.
        """
        for key, value in json.items():
            self.__setattr__(key, value)
