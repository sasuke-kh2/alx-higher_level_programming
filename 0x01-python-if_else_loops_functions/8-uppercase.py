#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    counter = 0
    for lo in range(length):
        if ord(str[counter]) > 96 and ord(str[counter]) < 123:
            num = ord(str[counter]) - 32
        else:
            num = ord(str[counter])
        print("{}".format(chr(num)), end="")
        counter = counter + 1
    print("{}".format("\n"), end="")
