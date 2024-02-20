#!/usr/bin/python3
"""Gets todos from jsonplaceholder for a specified employee."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emps = requests.get(url + "users/{}".format(sys.argv[1])).json()
    td_lt = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open(f"{user_id}.csv", 'w', newline='') as csv_doc:
        write_to_csv = csv.writer(csv_doc, quoting=csv.QUOTE_ALL)
        [write_to_csv.writerow(
            [user_id, username, td.get('completed'), td.get('title')]
            ) for task in td_lt]
