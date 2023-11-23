# TODO решите задачу
import json


filename_ = "input.json"


def task() -> float:
    with open(filename_, "r") as f:
        json_data = json.load(f)
    values_ = [item["score"] * item["weight"] for item in json_data]
    return round(sum(values_), 3)


print(task())
