import json
import os

def display(expense_list):
    if expense_list:
        print(f"{'ID':<5} {'Expense':<20} {'Amount':<10}")
        print("-" * 30)
        for i, expense in enumerate(expense_list, start=1):
            print(f"{i:<5} {expense['expense']:<20} ${expense['amount']:<10}")
    else:
        print("No data found.")

