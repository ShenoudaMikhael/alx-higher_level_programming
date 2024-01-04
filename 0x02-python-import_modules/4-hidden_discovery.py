#!/usr/bin/python3
import sys

for i in list(dir(sys.argv)):
    if i[:2] == "__":
        continue
    print("{0}".format(i))
