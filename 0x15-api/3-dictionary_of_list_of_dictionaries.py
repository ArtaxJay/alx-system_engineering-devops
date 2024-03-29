#!/usr/bin/python3
"""Gets todos from jsonplaceholder for a specified employee."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emps = requests.get(url + "users").json()

    with open("todo_all_employees.json", 'w') as json_doc:
        json.dump({
            emp.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": emp.get("username")
                } for task in requests.get(url + "todos",
                                           params={"userId": emp.get("id")}).
                json()]
            for emp in emps}, json_doc)
