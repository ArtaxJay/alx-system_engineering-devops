#!/usr/bin/python3
"""Gets todos from jsonplaceholder for a specified employee."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    emps = requests.get(url + "users/{}".format(user_id)).json()
    td_lt = requests.get(url + "todos", params={"userId": user_id}).json()
    emps_username = emps.get("username")

    with open(f"{user_id}.json", 'w') as json_file:
        """ Export data to a json file"""
        json.dump({user_id: [{
                "task": td.get("title"),
                "completed": td.get("completed"),
                "username": emps_username
                } for td in td_lt]}, json_file)
