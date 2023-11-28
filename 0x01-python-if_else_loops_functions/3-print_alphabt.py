#!/usr/bin/python3
for alphabet in range(26):
    if chr(alphabet + 97) != 'e' and chr(alphabet + 97) != 'q':
        print("{:c}".format(alphabet + 97), end="")
