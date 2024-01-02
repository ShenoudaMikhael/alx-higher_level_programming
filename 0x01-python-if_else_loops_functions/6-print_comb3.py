#!/usr/bin/python3
num_list = [str(x) + str(y) for x in range(10) for y in range(10) if y > x]
for s in range(len(num_list)):
    print(
        "{}".format(num_list[s]),
        end=", " if num_list[s] != "89" else None,
    )
