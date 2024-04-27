#!/usr/bin/python3
""" 7. Error code #1 """
import sys
import requests

if __name__ == "__main__":

    with requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": sys.argv[1] if len(sys.argv) > 1 else ""},
        timeout=30,
    ) as r:
        try:
            res = r.json()
            if res == {}:
                print("No result")
            elif res != {}:
                print("[{}] {}".format(res["id"], res["name"]))
        except Exception:
            print("Not a valid JSON")
