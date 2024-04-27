#!/usr/bin/python3
""" 5. Response header value #1 """
import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers["X-Request-Id"])
