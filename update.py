import json
import os
import display

def update():
    filename="expenses.json"
    if os.path.exists(filename):
        with open(filename,"r") as file:
            try:
                expense_list=json.load(file)
            except json.JSONDecodeError:
                expense_list=[]
            if expense_list:
                display.display(expense_list)
    else:
        expense_list=[]
        
    while(True):
        expense_id = int(input("Enter the expense ID to update (or type '0' to quit): "))
        if expense_id == 0:
            break
        if len(expense_list) < expense_id or expense_id < 1:
            print("Invalid ID. Please try again.")
            continue
        else:
            add_amount= float(input("Enter the amount:  "))
            expense_list[expense_id - 1]['amount'] += add_amount
        
    with open(filename, "w") as file:
        json.dump(expense_list, file)