#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    counter = len(argv)
    count = 0
    if counter == 1:
        print("{} arguments.".format(counter - 1))
    else:
        if counter == 2:
            print("{} argument:".format(counter - 1))
            for count in range(counter):
                if count == 0:
                    continue
                print("{}: {}".format(count, argv[count]))
        else:
            print("{} arguments:".format(counter - 1))
            for count in range(counter):
                if count == 0:
                    continue
                print("{}: {}".format(count, argv[count]))
