#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for i in list(dir(hidden_4)):
        if i[:2] == "__":
            continue
        print("{0}".format(i))
