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
        self.value = value
        self.name = name
        if not isinstance(self.value, int):
            raise TypeError("{} must be an integer".format(name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
