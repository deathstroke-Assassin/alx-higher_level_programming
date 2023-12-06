#!/usr/bin/python3
def number_keys(a_dictionary):
    x = 0
    k = list(a_dictionary.keys())
    for a in k:
        x += 1
    return x
