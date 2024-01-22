#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    try:
        for i in range(x):
            print("{0}".format(my_list[i]), end="")
            z += 1
    except Exception:
        pass
    print("")

    return z
