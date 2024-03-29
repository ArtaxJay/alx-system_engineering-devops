#!/usr/bin/python3
"""Gets todos from jsonplaceholder for a specified employee."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    emps = requests.get(url + "users/{}".format(user_id)).json()
    td_lt = requests.get(url + "todos", params={"userId": user_id}).json()
    emps_username = emps.get("username")

    with open(f"{user_id}.csv", 'w', newline='') as csv_doc:
        write_to_csv = csv.writer(csv_doc, quoting=csv.QUOTE_ALL)
        [write_to_csv.writerow(
            [user_id, emps_username, task.get('completed'), task.get('title')]
            ) for task in td_lt]
