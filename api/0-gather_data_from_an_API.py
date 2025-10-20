#!/usr/bin/python3
"""
Gather data from an API: Returns TODO list progress for a given employee ID
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays employee TODO list progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = 0
    completed_titles = []
    for task in todos_data:
        if task.get("completed"):
            completed_tasks += 1
            completed_titles.append(task.get('title'))
    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")
    for title in completed_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    # Fetch user
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user = requests.get(user_url).json()
    employee_name = user.get("name")

    # Fetch todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos = requests.get(todos_url).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_done = len(done_tasks)

    # Print in exact format
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
