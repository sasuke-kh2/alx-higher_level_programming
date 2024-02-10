#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for pr in my_list:
        try:
            if pr == my_list[x]:
                break
        except IndexError:
            x = x
        try:
            print("{:d}".format(pr), end="")
            counter = counter + 1
        except IndexError:
            break
        except TypeError:
            continue
        except ValueError:
            continue
    print()
    return counter
