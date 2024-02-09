#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    calc = 0
    count = 1
    if len(argv) == 1:
        print(calc)
    else:
        while count < (len(argv)):
            calc = calc + int(argv[count])
            count = count + 1
        print(calc)
