#!/usr/bin/python3
"""Python script that for a given employee ID, returns information
about his/her TODO list progress."""

import csv
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
    user_id = employee_request.get('id')
    comp_tasks = [(user_id, name, task['completed'],
                   task['title']) for task in todo_request]
    file_name = f'{user_id}.csv'

    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASKS_COMPLETED_STATUS',
                        'TASK_TITLE'])
        writer.writerows(comp_tasks)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_info(employee_id)
