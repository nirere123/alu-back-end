#!/usr/bin/python3

"""gather data from an api"""
import requests
import sys


def main():
    """Fetch and display TODO progress for a given employee id."""
    if len(sys.argv) != 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except (ValueError, TypeError):
        return

    # Fetch todos for the user (note: endpoint must be /users/ not /user/)
    response_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )
    data = response_todos.json()

    completed_tasks = []
    for item in data:
        if item.get('completed'):
            completed_tasks.append(item.get('title'))

    # Fetch user info
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()

    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(completed_tasks), len(data)))

    for task in completed_tasks:
        print("\t " + task)


if __name__ == '__main__':
    main()
