#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in new_list:
        if i == search:
            i -= 1
            new_list[i] = replace
            return new_list
