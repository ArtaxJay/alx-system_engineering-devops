#!/usr/bin/python3
"""Gets todos from jsonplaceholder for a specified employee."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emps = requests.get(url + "users/{}".format(sys.argv[1])).json()
    td_lt = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open(f"{user_id}.json", 'w') as json_file:
        """ Export data to a json file"""
        json.dump({user_id: [{
                "task": td.get("title"),
                "completed": td.get("completed"),
                "username": username
                } for td in td_lt]}, json_file)
