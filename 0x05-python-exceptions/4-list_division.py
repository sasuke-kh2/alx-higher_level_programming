#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    x = 0
    while x < list_length:
        try:
            result.append(my_list_1[x] / my_list_2[x])
            x = x + 1
        except TypeError:
            result.append(0)
            print("wrong type")
            x = x + 1
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
            x = x + 1
        except IndexError:
            result.append(0)
            print("out of range")
            x = x + 1
        finally:
            result = result
    return result
