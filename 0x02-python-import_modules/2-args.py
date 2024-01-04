#!/usr/bin/python3
# File 2-args.py
if __name__ == "__main__":
    import sys

    print(
        "{0} {1}{2}".format(
            len(sys.argv) - 1,
            "argument" if len(sys.argv) == 2 else "arguments",
            ":" if len(sys.argv) != 1 else ".",
        )
    )
    for i, v in list(enumerate(sys.argv))[1:]:
        print("{0}: {1}".format(i, v))
