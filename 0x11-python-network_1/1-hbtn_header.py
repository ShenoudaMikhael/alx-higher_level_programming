#!/usr/bin/python3
""" 1. Response header value #0  """
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    body = response.read()
    print(response.headers["X-Request-Id"])
