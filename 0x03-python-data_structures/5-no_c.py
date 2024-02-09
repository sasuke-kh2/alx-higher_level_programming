#!/usr/bin/python3
def no_c(my_string):
    Cc = "Cc"
    upstr = ""
    for x in range(len(my_string)):
        if my_string[x] != Cc[0] and my_string[x] != Cc[1]:
            upstr = upstr + my_string[x]
        else:
            continue
    return upstr
