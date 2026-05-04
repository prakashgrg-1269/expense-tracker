import json
import os

def add():
    filename="expenses.json"
    if os.path.exists(filename):
        with open(filename,"r") as file:
            try:
                expense_list=json.load(file)
            except json.JSONDecodeError:
                expense_list=[]
    else:
        expense_list=[]
        
    while(True):
        expense = input("Enter the expense (or type 'exit' to quit): ")
        if expense.lower() == 'exit':
            break
        amount = float(input("Enter the amount: "))
        expense_list.append({"expense": expense, "amount": amount})

    with open(filename, "w") as file:
        json.dump(expense_list, file)
