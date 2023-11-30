#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = len(sys.argv)
    sum = 0
    for i in range(1, arg):
        sum += int(sys.argv[i])
    print("{}".format(sum)))
