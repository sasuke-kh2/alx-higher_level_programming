#!/usr/bin/python3
"""class module
"""


class MyList(list):
    """class that takes a list as anrgument as
        inhertance
    """
    def print_sorted(self):
        """print the list sorted"""
        list2 = self.copy()
        list2.sort()
        print(list2)
