#!/usr/bin/python3
def uppercase(str):
    UP = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            UP += chr(ord(c) - 32)
            print("{:s}".format(UP))
        else:
            UP += chr(ord(c))
            print("{:s}".format(UP))
