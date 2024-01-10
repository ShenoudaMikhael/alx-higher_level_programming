#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    q = dict(my_list)
    d_sum = 0
    d_div = 0
    for k, v in q.items():
        d_sum += k * v
        d_div += v

    return d_sum / d_div
