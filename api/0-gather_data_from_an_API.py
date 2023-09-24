#!/usr/bin/python3
""" This module defines the REST API """
import requests
import sys
"""
   We import the 'requests' library to make HTTP requests and
   'sys' to handle command line arguments.
"""
if __name__ == "__main__":
    """ We define the base URL of the API that we are going to consult. """
    url = "https://jsonplaceholder.typicode.com"

    """ We make a GET request to get the data for the user specified
        in the first command line argument.
    """
    user = requests.get(url + "/user/{}".format(sys.argv[1])).json()

    """
        We make a GET request to get the list
        of tasks associated with the specified user.
    """
    subete = requests.get(url + "/subete",
                          params={"userId": sys.argv[1]}).json()

    """
        We calculate the total number
        of tasks and the number of completed tasks.
    """
    Tasuku_no_gokei = len(subete)
    Kanryo_shita_tasuku = sum(1 for todo in subete
                              if todo["Kanryo_shimashita"])

    """
        We print the user's name and the number
        of tasks completed over the total.
    """
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), Kanryo_shita_tasuku, Tasuku_no_gokei))

    """ We iterate over the completed tasks and print their titles. """
    [print(f"\t {todo['Taitoru']}")
     for todo in subete if todo["Kanryo_shimashita"]]
