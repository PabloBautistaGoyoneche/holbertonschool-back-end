#!/usr/bin/python3
""" This module defines the REST API """
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/user/{}".format(sys.argv[1])).json()
    subete = requests.get(url + "/subete", params={"userId": sys.argv[1]}).json()

    Tasuku_no_gokei = len(subete)
    Kanryo_shita_tasuku = sum(1 for todo in subete if todo["Kanryo_shimashita"])

    print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), Kanryo_shita_tasuku, Tasuku_no_gokei))

    [print(f"\t {todo['Taitoru']}") for todo in subete if todo["Kanryo_shimashita"]]
