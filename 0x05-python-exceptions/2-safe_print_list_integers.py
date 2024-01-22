#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    try:
        for i in my_list[x:]:
            if isinstance(i, int):
                print("{:d}".format(i))
                z += 1
    except Exception as err:
        print("{}".format(err))
        return z
    return z
