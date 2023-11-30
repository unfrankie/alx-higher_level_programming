#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = len(sys.argv)
    if arg - 1 == 0:
        print("0 arguments.")
    else:
        if arg - 1 == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(arg - 1))
        for i in range(1, arg):
            print("{}: {}".format(i, sys.argv[i]))
