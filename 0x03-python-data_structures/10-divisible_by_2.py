#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tf_list = []
    for num in my_list:
        if num % 2 == 0:
            tf_list.append(True)
        else:
            tf_list.append(False)
    return tf_list
