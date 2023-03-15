#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortKeys = list(a_dictionary.keys())
    sortKeys.sort()
    sorted_dict = {i: a_dictionary[i] for i in sortKeys}
    print(sorted_dict)
