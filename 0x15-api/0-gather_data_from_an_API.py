#!/usr/bin/python3
"""Returns info about employee's todo list progress."""

import requests
import sys


if __name__ == '__main__':
    empId = sys.argv[1]
    userUrl = "https://jsonplaceholder.typicode.com/users/"
    userInfo = userUrl + empId
    taskInfo = userUrl + empId + "/todos"

    # Send API requests
    userResponse = requests.get(userInfo)
    taskResponse = requests.get(taskInfo)

    # Get employee name from userResponse
    empName = userResponse.json().get('name')

    # Get tasks from taskResponse as todos
    todos = taskResponse.json()

    # Store number of todos in a variable allTasks
    allTasks = len(todos)

    # Create storage array for completed todos
    compTasks = []

    # Create counter for completed todos
    comp = 0

    for item in todos:
        if item['completed'] is True:
            compTasks.append(item)
            comp += 1

    print(f'Employee {empName} is done with tasks({comp}/{allTasks}):')
    for item in compTasks:
        print(f'\t {item["title"]}')
