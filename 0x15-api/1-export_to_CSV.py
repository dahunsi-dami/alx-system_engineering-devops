#!/usr/bin/python3
"""
Returns info about employee's todo list progress,
and export data in CSV format.
"""

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

    fname = f'{sys.argv[1]}.csv'

    with open(fname, "w") as file:
        for item in todos:
            comp = item['completed']
            title = item['title']
            file.write(f'"{empId}", "{empUName}", "{comp}", "{title}"\n')
