import json
import os

with open("tasks.json") as f:
    tasks = json.load(f)
    data = tasks["tasks"]
    print(data)
