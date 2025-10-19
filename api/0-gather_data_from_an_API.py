#!/usr/bin/python3

"""gather data from an api"""
import requests
import sys


def main(argv):
    """Gather TODO data for a given employee id and print progress.

    Expects a single integer argument (employee id).
    Output format must match the assignment exactly.
    """
    if len(argv) != 2:
        # require exactly one argument (script name + id)
        return 1

    try:
        emp_id = int(argv[1])
    except (TypeError, ValueError):
        return 1

    # Fetch todos for the user
    todos_resp = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos")
    try:
        todos = todos_resp.json()
    except ValueError:
        todos = []

    # Collect completed task titles
    completed = [t.get('title') for t in todos if t.get('completed')]

    # Fetch user info
    user_resp = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}")
    try:
        user = user_resp.json()
    except ValueError:
        user = {}

    name = user.get('name')
    # Print header line exactly as required
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed), len(todos)
    ))

    # Each completed task must be printed with one tab and one space before title
    for title in completed:
        print("\t " + title)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
