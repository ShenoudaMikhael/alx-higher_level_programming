#!/usr/bin/python3
# File 3-infinite_add.py
if __name__ == "__main__":
    import sys

    res = 0
    for i, v in list(enumerate(sys.argv))[1:]:
        res += int(v)
    print(res)
