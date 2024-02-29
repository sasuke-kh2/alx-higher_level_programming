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

    def integer_validator(self, name, value):
        """Public instance method  that validates value"""
        if value is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than".format(name))
