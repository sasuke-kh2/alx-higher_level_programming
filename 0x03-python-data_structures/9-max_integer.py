#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        num = 0
        for count in my_list:
            if int(count) > num:
                num = count
        return int(num)
