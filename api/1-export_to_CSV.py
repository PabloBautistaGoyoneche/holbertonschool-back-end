#!/usr/bin/python3
""" This module defines the REST API """

"""
    We import the necessary libraries: 'csv' to work with
    CSV files, 'requests' to make HTTP requests and 'sys'
    to handle command line arguments.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    """ We define the base URL of the API that we are going to consult. """
    url = "https://jsonplaceholder.typicode.com"
    
    """ 
        We make a GET request to obtain
        the data of the user specified in the first
        command line argument.
    """
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    
    """ 
        We make a GET request to obtain the
        list of tasks associated with the specified user.
    """
    modu = requests.get(url + "/todos", params={"userId": sys.argv[1]}).json()
    
    """ 
        We generate the name of the CSV file
        based on the user ID.
    """ 
    fairu_mei = "{}.csv".format(user["id"])
    
    """ 
        We open the CSV file in writing mode and
        we configure the CSV writer.
    """
    with open(fairu_mei, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    
        """ 
            We iterate over the tasks and write
            each record in the CSV file.
        """
        for todo in modu:
            user_id = user["id"]
            username = user["username"]
            completed = str(todo["completed"])
            title = todo["title"]
            writer.writerow([user_id, username, completed, title])
