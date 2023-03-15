#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common_set = set_1 ^ set_2
    return sorted(list(common_set))
