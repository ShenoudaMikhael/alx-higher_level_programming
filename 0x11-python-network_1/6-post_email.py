#!/usr/bin/python3
""" 6. POST an email #1 """
import sys
import requests

if __name__ == "__main__":
    with requests.post(
            sys.argv[1],
            data={"email": sys.argv[2]},
            timeout=30
            ) as r:
        print(r.text)
