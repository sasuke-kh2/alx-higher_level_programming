#!/usr/bin/python3
"""Alx module
    this module contains Rectangle class

"""

class Rectangle:
    """this is Rectangle class.

    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    def height(self):
        return self.__height
    def height(self, value):
        if isinstance(value, str):
            raise TypeError("__height must be an integer")
        elif isinstance(value, float):
            raise TypeError("__height must be an integer")
        elif int(value) < 0:
            raise ValueError("__height must be >= 0")
        else:
            self.__height = value
    def width(self):
        return self.__width
    def width(self, value):
        if isinstance(value, str):
            raise TypeError("__width must be an integer")
        elif isinstance(value, float):
            raise TypeError("__width must be an integer")
        elif int(value) < 0:
            raise ValueError("__width must be >= 0")
        else:
            self.__width = value
