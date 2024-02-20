#!/usr/bin/python3
"""this moudle containes Rectangle class"""


class Rectangle:
    """Rectangle class."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """prints message when a Rectangle is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area methode"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self):
        """Return a string representation of the rectangle."""
        result = ""
        if self.width == 0 or self.height == 0:
            result = ""
        else:
            for _ in range(self.height):
                result += "#" * self.width
                if _ < self.height - 1:
                    result += "\n"
        return result
