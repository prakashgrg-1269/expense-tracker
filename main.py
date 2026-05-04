import json
import os
import display
import add
import update   
import delete
while(True):
    print("""
1. To display all expenses.
2. To add an expense.
3. To update status of a expense.
4. To To delete a expense
5. To exit """)
    try:
        choice=int(input("Enter 1, 2, 3, 4 or 5: "))
    except ValueError:
        print("you can only enter interger")
        continue
    if choice==1:
        filename="expenses.json"
        if os.path.exists(filename):
            with open(filename,"r") as file:
                try:
                    expense_list=json.load(file)
                except json.JSONDecodeError:
                    expense_list=[]
                if expense_list:
                    display.display(expense_list)
    elif choice==2:
        add.add()
    elif choice==3:
        update.update()
    elif choice==4:
        delete.delete()
    elif choice==5:
        print("exiting")
        break
    else:
        print("you only enter an integer from 1-5")

    
