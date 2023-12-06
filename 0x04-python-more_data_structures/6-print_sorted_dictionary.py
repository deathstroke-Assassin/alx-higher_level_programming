#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dix = list(a_dictionary.keys())
    dix.sort()
    for k in dix:
        print("{}: {}".format(k, a_dictionary.get(k)))
