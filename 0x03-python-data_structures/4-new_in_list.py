#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list:
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        nw_list = my_list.copy
        nw_list[idx] = element
        return nw_list
