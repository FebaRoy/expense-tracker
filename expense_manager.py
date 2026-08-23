from utils import valid_input
from file_manager import update_expenses

def add_expenses(expenses, categories):
    n = valid_input("Enter the number of expenses you want to add: ")
    for i in range(n):
        try: 
            expense = float(input(f"Enter your expense {i+1}: "))
            category = input(f"Enter the category of your expense {i+1}: ")
            if expense > 0:
                if expense > 1000:
                    print(f"{expense} is a high expense.")
                with open("expenses.txt", "a") as file:
                    file.write(f"{category} | {expense}\n")
                    print("Expense Recorded!")
            else:
                print("Expense must be greater than 0.")
        except ValueError:
            expense = float(input(f"Enter your valid expense {i+1}: "))
            category = input(f"Enter the category of your expense {i+1}: ")
            if expense > 0:
                if expense > 1000:
                    print(f"{expense} is a high expense.")
                with open("expenses.txt", "a") as file:
                    file.write(f"{category} | {expense}\n")
                    print("Expense Recorded!")
            else:
                print("Expense must be greater than 0.")
    update_expenses(expenses, categories)

def category_search(categories, expenses):
    target = input("Enter the category to search: ")
    total = 0
    for i in range(len(categories)):
        if categories[i].lower() == target.lower():
            print(f"{target} | {expenses[i]}")
            total += expenses[i]
    if total == 0:
        print("No expenses found.")
    else:
        print(f"Total {target} expenses: {total}")
