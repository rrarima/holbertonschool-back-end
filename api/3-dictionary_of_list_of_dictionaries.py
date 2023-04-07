#!/usr/bin/python3
"""API request for employee name and todos completed"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users").json()
    all_todos = {}

    for user in users:
        user_id = user['id']
        todos = requests.get(url + "/todos", params={"userId": user_id}).json()
        user_todos = [{"username": user["username"], "task": todo["title"],
                       "completed": todo["completed"]} for todo in todos]
        all_todos[user_id] = user_todos

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(all_todos, outfile)
