name = input("Enter your name: ")
expenses = []
categories = []

def update_expenses():
    categories.clear()
    expenses.clear()
    with open("expenses.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            categories.append(line.split('|')[0].strip())
            expenses.append(float(line.split('|')[1].strip()))

def add_expenses():
    n = int(input("Enter the number of expenses you want to add: "))
    for i in range(n):
        expense = float(input(f"Enter your expense {i+1}: "))
        category = input(f"Enter the category of your expense {i+1}: ")
        if expense > 1000:
            print(f"{expense} is a high expense.")
        with open("expenses.txt", "a") as file:
            file.write(f"{category} | {expense}\n")
    update_expenses()
    print("Expense Recorded!")

def show_expenses():
    with open("expenses.txt", "r") as file:
        print(file.read())
    file.close()
    
def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

def count_expenses(expenses):
    return len(expenses)

def max_expense(expenses):
    highest_expense = 0
    for expense in expenses:
        if expense > highest_expense:
            highest_expense = expense
    return highest_expense

def category_search(categories):
    target = input("Enter the category to search: ")
    total = 0
    for i in range(len(categories)):
        if categories[i].lower() == target.lower():
            print(f"{target} | {expenses[i]}")
            total += expenses[i]
    print(f"Total {target} expenses: {total}")

def delete_all_expenses():
    with open("expenses.txt","w") as file:
        file.write("")
    print("All your expenses are deleted.")

def menu(expenses, categories):
    print("------MENU------")
    print("1. Add Expenses")
    print("2. Show Expenses")
    print("3. Total Expenses")
    print("4. Count Expenses")
    print("5. Max Expense")
    print("6. Category Search")
    print("7. Delete All Expenses")
    print("8. Exit")
    
    option = int(input("Enter your choice: "))
    
    if option == 1:
        add_expenses()
        
    elif option == 2:
        show_expenses()
    
    elif option == 3:
        print(f"Total Expenses: {total_expenses(expenses)}")
        print()
    
    elif option == 4:
        print(f"You recorded {count_expenses(expenses)} expenses.")
    
    elif option == 5:
        print(f"Highest Expense: {max_expense(expenses)}")
    
    elif option == 6: 
        category_search(categories)
    
    elif option == 7:
        delete_all_expenses()
        
    elif option == 8:
        exit()
        
    else:
        print("Invalid choice. Try again.")

while True:
    update_expenses()
    menu(expenses, categories)