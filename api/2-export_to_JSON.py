#!/usr/bin/python3
"""API request for employee name and todos completed"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(user_id)).json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    user_todos = [{"task": todo["title"], "completed": todo["completed"],
                   "username": user["username"]} for todo in todos]

    output_data = {user_id: user_todos}

    with open(f"{user_id}.json", "w") as outfile:
        json.dump(output_data, outfile)
