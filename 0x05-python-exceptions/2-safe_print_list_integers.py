#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                z += 1
        print("")

    except IndexError as e:
        raise e

    return z
