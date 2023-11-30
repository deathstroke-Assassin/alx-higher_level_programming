#!/usr/bin/python3
for i in range(1, 9):
    for x in range(0, 10):
        if i > x:
            print("{:d}{:d}, ".format(i, x),end="")
        elif (i == 9 and x == 8) or (i == 8 and x == 9):
            print("{:d}{:d}".format(i, x))
