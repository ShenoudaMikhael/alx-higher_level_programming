#!/usr/bin/python3
# File 2-args.py
if __name__ == "__main__":
    import sys

    print(
        "{0} argument{1}{2}".format(
            len(sys.argv) - 1,
            "s" if len(sys.argv) > 2 else "",
            ":" if len(sys.argv) > 2 else ".",
        )
    )
    for i, v in list(enumerate(sys.argv))[1:]:
        print("{0}: {1}".format(i, v))
