#!/usr/bin/python3
""" 3. Error code #0 """
import sys
import urllib.request

if __name__ == "__main__":

    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode("utf8"))
    except urllib.error.HTTPError as e:

        print("Error code: {}".format(e.code))
