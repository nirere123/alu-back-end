#!/usr/bin/python3
"""
Module for fetching employee TODO list progress from REST API
"""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]

    # Get user info
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()
    employee_name = user.get("name")

    # Get TODO list
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    ).json()

    # Filter completed tasks
    completed_tasks = [
        task.get("title") for task in todos if task.get("completed")
        ]

    # Print output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos))
    )
    for task in completed_tasks:
        print("\t {}".format(task))
