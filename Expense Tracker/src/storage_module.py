import json
import os


FILE_PATH = "expenses.json" # stored in project root


def load_expenses():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except:
        return []




def save_expenses(expenses):
    with open(FILE_PATH, "w") as f:
        json.dump(expenses, f, indent=2)