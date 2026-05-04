import json
import os
import display

def delete():
    while(True):
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
        
        expense_id = int(input("Enter the expense ID to delete (or type '0' to quit): "))
        if expense_id == 0:
            break
        if len(expense_list) < expense_id or expense_id < 1:
            print("Invalid ID. Please try again.")
            continue
        else:
            expense_list.pop(expense_id - 1)
            print("Expense deleted successfully.")

        with open(filename, "w") as file:
            json.dump(expense_list, file)
