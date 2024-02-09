#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        num = 0
        num2 = 0
        for count in my_list:
            num += count[0] * count[1]
            num2 += count[1]
        nu = num / num2
        return nu
