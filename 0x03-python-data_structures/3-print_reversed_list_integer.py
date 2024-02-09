#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        count = len(my_list)
        while count > 0:
            print("{:d}".format(int(my_list[count - 1])))
            count = count - 1
