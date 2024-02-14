#!/usr/bin/python3
"""Square module.

The Square module contains class called Square
"""


class Square:
    """Square class

    this class contains Private instance attribute: size.
    """
    def __init__(self, __size=0):
        """Private instance attribute

        """
        self.__size = __size
        if isinstance(__size, str):
            raise TypeError("size must be an integer")
        elif int(__size) < 0:
            raise ValueError("size must be >= 0")
