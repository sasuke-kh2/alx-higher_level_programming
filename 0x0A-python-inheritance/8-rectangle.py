#!/usr/bin/python3
"""This module includes the below class"""


class BaseGeometry:
    """Not an empty class"""
    def area(self):
        """Public instance method that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value."""
        self.name = name
        self.value = value

        # Check if value is an integer
        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(self.name))

        # Check if value is greater than 0
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
