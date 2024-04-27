#!/usr/bin/python3
""" 7. Error code #1 """
import sys
import requests

if __name__ == "__main__":

    with requests.get(sys.argv[1], timeout=30) as r:
        try:
            r.raise_for_status()
            print(r.text)
        except Exception:
            print("Error code: {}".format(r.status_code))
