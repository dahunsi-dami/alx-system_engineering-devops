#!/usr/bin/python3
"""
Returns info about all employee's todo list,
and export data in json format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    userUrl = "https://jsonplaceholder.typicode.com/users/"

    # Send API request
    userResponse = requests.get(userUrl)

    # Collect employees dict from UserResponse
    emps = userResponse.json()

    valoos = {}

    for e in emps:
        eId = e['id']
        eUName = e['username']
        taskInfo = userUrl + str(eId) + "/todos"
        taskResponse = requests.get(taskInfo)
        todos = taskResponse.json()
        valoos[eId] = []
        for item in todos:
            valoos[eId].append({
                "task": item['title'],
                "completed": item['completed'],
                "username": eUName
            })

    fname = 'todo_all_employees.json'

    with open(fname, "w") as file:
        json.dump(valoos, file)
