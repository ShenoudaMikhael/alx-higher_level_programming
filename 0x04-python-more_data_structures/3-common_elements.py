#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = list(set_1)
    my_list.extend(list(set_2))
    return set([i for i in my_list if my_list.count(i) > 1])
