#!/usr/bin/python3
""" 9. My GitHub! """
import sys
import requests

if __name__ == "__main__":

    url = "https://api.github.com/users/{}".format(sys.argv[1])
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    headers["Authorization"] = "Bearer {}".format(sys.argv[2])

    response = requests.get(url, headers=headers)
    if "id" in response.json():
        print(response.json()["id"])
    else:
        print(None)
