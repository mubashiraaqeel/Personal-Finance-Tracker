import json


def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            monthly_budget = data["monthly_budget"]
            transactions = data["transactions"]
            return monthly_budget, transactions
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []


def save_data(transactions, monthly_budget):
    with open("data.json", "w") as file:
        data = {
            "monthly_budget": monthly_budget,
            "transactions": transactions
        }
        json.dump(data, file, indent=4)
       
        