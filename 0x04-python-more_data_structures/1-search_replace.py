#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda k: replace if k == search else k, my_list))
    return new_list
