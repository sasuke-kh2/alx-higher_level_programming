#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def check(x):
        if x == search:
            return replace
        else:
            return x
    my_list2 = list(map(check, my_list.copy()))
    return my_list2
