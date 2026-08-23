import os

def valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. {prompt}")
    
def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')    

def show_menu():
    print("------MENU------")
    print("1. Add Expenses")
    print("2. Show Expenses")
    print("3. Total Expenses")
    print("4. Count Expenses")
    print("5. Max Expense")
    print("6. Category Search")
    print("7. Delete All Expenses")
    print("8. Exit")
    print("9. Clear Screen")
