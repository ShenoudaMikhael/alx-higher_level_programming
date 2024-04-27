#!/usr/bin/python3
""" 9. My GitHub! """
import sys
import requests

if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2])
    headers = {
        "Accept": "application/vnd.github+json",
        # "Authorization": "",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    # headers["Authorization"] = "Bearer {}".format(sys.argv[2])

    response = requests.get(url, headers=headers)
    a = response.json()

    # i = 0
    # for aa in list(a).reverse():

    #     print("{} {}".format(aa["sha"], aa["commit"]["author"]["name"]))
    #     i += 1
    #     if i == 10:
    #         break
    q = len(a)
    i = 0

    for i in range(10):
        q = q - 1
        print("{} {}".format(a[q]["sha"], a[q]["commit"]["author"]["name"]))
