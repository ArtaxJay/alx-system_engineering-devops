#!/usr/bin/python3
"""Gets todos from jsonplaceholder for a specified employee."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emps = requests.get(url + "users/{}".format(sys.argv[1])).json()
    td_lt = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    response = \
        [td.get("title") for td in td_lt if td.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        emps.get("name"), len(response), len(td_lt)))
    [print("\t {}".format(each)) for each in response]
