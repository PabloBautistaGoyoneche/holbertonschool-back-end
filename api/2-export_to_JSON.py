#!/usr/bin/python3
""" This module defines the REST API """
import json
import requests
import sys
"""
    We import the necessary libraries: 'json' to work with JSON,
    'requests' to make HTTP requests and 'sys' to handle
    command line arguments.
"""
if __name__ == "__main__":
    """ We define the base URL of the API that we are going to consult. """
    url = "https://jsonplaceholder.typicode.com"

    """
        We get the user ID from the arguments
        command line.
    """
    yuza_id = sys.argv[1]

    """
        We make a GET request to obtain the
        data of the specified user.
    """
    user = requests.get(url + "/users/{}".format(yuza_id)).json()

    """
        We make a GET request to get the list
        of tasks associated with the specified user.
    """
    modu = requests.get(url + "/todos", params={"userId": yuza_id}).json()

    """
        We create a list of dictionaries that represent
        user tasks with relevant information.
    """
    yuza_modu = [{"task": todo["title"], "completed": todo["completed"],
                  "username": user["username"]} for todo in modu]

    """
        We create a dictionary that contains the
        user information and tasks.
    """
    Shutsuryoku_deta = {yuza_id: yuza_modu}

    """
        We write the dictionary to a JSON file
        with the user's name as the file name.
    """
    with open(f"{yuza_id}.json", "w") as outfile:
        json.dump(Shutsuryoku_deta, outfile)
