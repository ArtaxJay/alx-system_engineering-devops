#!/usr/bin/python3
"""Gets todos from jsonplaceholder for a specified employee"""
import requests
import sys


def get_user_info(user_id):
    """Get user information based on user ID."""
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()
    return user_data


def get_user_todos(user_id):
    """Get completed tasks for a given user ID."""
    url = "https://jsonplaceholder.typicode.com/"
    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos_data = todos_response.json()
    """
    completed_tasks = [todo.get("title") for todo in todos_data
                       if todo.get("completed")]
    """
    return todos_data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_info = get_user_info(user_id)
    todos_data = get_user_todos(user_id)
    completed_tasks = [todo.get("title") for todo in
                       todos_data if todo.get("completed")]
    total_tasks = len(completed_tasks) + len(todos_data)

    print("Employee {} is done with tasks ({}/{}):".format(
        user_info.get("name"), len(completed_tasks),
        total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task))
