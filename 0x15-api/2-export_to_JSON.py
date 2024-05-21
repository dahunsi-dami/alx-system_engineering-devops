#!/usr/bin/python3
"""
Returns info about employee's todo list progress,
and export data in json format.
"""

import json
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
    empUName = userResponse.json().get('username')

    # Get tasks from taskResponse as todos
    todos = taskResponse.json()

    fname = f'{sys.argv[1]}.json'

    valoos = {empId: []}

    for item in todos:
        valoos[empId].append({
            "task": item['title'],
            "completed": item['completed'],
            "username": empUName
        })

    with open(fname, "w") as file:
        json.dump(valoos, file)
