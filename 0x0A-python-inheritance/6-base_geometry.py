#!/usr/bin/python3
"""this moudule includes
    the bellow class"""


class BaseGeometry:
    """not an empty class"""
    def area(self):
        """Public instance method  that raises an
            Exception with the a message
        """
        raise Exception("area() is not implemented")
