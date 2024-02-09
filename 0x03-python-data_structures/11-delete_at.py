#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list):
        return my_list
    elif idx < 0:
        return my_list
    else:
        new_list = my_list.copy()
        my_list.clear()
        for count in new_list:
            if count == new_list[idx]:
                continue
            my_list.append(count)
        return my_list
