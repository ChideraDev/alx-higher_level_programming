#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_lst = my_list[::-1]
    for element in new_lst:
        print('{:d}'.format(element))
