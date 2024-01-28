#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = ""
    for c in text.strip():
        if c in ".?:":
            new += c + ("\n\n" if c != text.strip()[-1] else "")
        else:
            if c == " " and new[-3] in ".?:":
                continue
            new += c
    print(new, end="")
