#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        revlist = my_list
        revlist.reverse()
        for x in revlist:
            print("{:d}".format(x))
