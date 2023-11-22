#!/usr/bin/python3
"""Python script that for a given employee ID, returns information
about his/her TODO list progress."""

import json
import requests
import sys


def employee_info(employee_id):
    """Given employee ID, returns information
about his/her TODO list progress."""

    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{url}/users/{employee_id}'
    todo_url = f'{url}/todos'

    employee_request = requests.get(employee_url).json()
    todo_request = requests.get(todo_url,
                                params={'userId': employee_id}).json()
    name = employee_request.get('name')
    comp_tasks =[task for task in todo_request if task ['completed']]

    tasks = [{'task': task['title'], 'completed':
             task['completed'], 'username': name} for task in comp_tasks]
    data = {employee_id: tasks}

    with open(f'{employee_id}.json', mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_info(employee_id)
