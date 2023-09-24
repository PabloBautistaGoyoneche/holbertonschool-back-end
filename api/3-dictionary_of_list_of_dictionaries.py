#!/usr/bin/python3
""" This module defines the REST API """

""" 
    We import the necessary libraries: 'json' to work with
    JSON and 'requests' to make HTTP requests.
"""
import json
import requests

if __name__ == "__main__":
    """
        We define the base URL of the API
        that we are going to consult.
    """
    url = "https://jsonplaceholder.typicode.com"
    
    """ We make a GET request to get the list of users. """
    Benotzer = requests.get(url + "/users").json()
    
    """ 
        We create an empty dictionary to store the
        task data of all users.
    """
    subete_modu = {}

    """ We iterate over the list of users. """
    for user in Benotzer:
        yuza_id = user['id']
        
        """
            We make a GET request to obtain the list of
            tasks associated with the current user.
        """
        modu = requests.get(url + "/todos", params={"userId": yuza_id}).json()
        
        """
            We create a list of dictionaries that represent
            the current user's tasks with relevant information.
        """
        user_todos = [{"username": user["username"], "task": 
                       todo["title"], "completed": todo["completed"]} 
                       for todo in modu]
        
        """
            We add the user's task list to
            main dictionary using its ID as a key.
        """
        subete_modu[yuza_id] = user_todos

    """ 
        We write the dictionary in a JSON file called
        "todo_all_employees.json".
    """
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(subete_modu, outfile)
