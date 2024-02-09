#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as op
    from sys import argv
    calc = 0
    if len(argv) == 4:
        if argv[2] == "+":
            calc = op.add(int(argv[1]), int(argv[3]))
            print("{} + {} = {}".format(argv[1], argv[3], calc))
        elif argv[2] == "-":
            calc = op.sub(int(argv[1]), int(argv[3]))
            print("{} - {} = {}".format(argv[1], argv[3], calc))
        elif argv[2] == "*":
            calc = op.mul(int(argv[1]), int(argv[3]))
            print("{} * {} = {}".format(argv[1], argv[3], calc))
        elif argv[2] == "/":
            calc = op.div(int(argv[1]), int(argv[3]))
            print("{} / {} = {}".format(argv[1], argv[3], calc))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
