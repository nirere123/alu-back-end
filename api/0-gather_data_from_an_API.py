#!/usr/bin/python3
"""
Module for fetching employee TODO list progress from REST API
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Get employee info
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()
    employee_name = user.get("name")

    # Get the employee's todo list
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()

    # Count completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]

    # Print in the required format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos))
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
