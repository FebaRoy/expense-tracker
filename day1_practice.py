name = input("Enter your name: ")
expenses = []
categories = []

file = open("expenses.txt", "a")

def add_expenses(expenses, categories):
    n = int(input("Enter the number of expenses you want to add: "))
    for i in range(n):
        expense = float(input(f"Enter your expense {i+1}: "))
        category = input(f"Enter the category of your expense {i+1}: ")
        if expense > 1000:
            print(f"{expense} is a high expense.")
        expenses.append(expense)
        categories.append(category)
        file = open("expenses.txt", "a")
        file.write(f"{categories[i]} | {expenses[i]}\n")
    print("Expense Recorded!")

def show_expenses(file):
    file = open("expenses.txt", "r")
    print(file.read())
    
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
    sum = 0
    for i in range(len(categories)):
        if categories[i].lower() == target.lower():
            print(f"{target} | {expenses[i]}")
            sum += expenses[i]
    print(f"Total {target} expenses: {sum}")

def menu(expenses, categories):
    print("------MENU------")
    print("1. Add Expenses")
    print("2. Show Expenses")
    print("3. Total Expenses")
    print("4. Count Expenses")
    print("5. Max Expense")
    print("6. Category Search")
    print("7. Exit")
    
    option = int(input("Enter your choice: "))
    
    if option == 1:
        add_expenses(expenses, categories)
        
    elif option == 2:
        show_expenses(file)
    
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
        exit()
    
    else:
        print("Invalid choice. Try again.")

file.close()

while True:
    menu(expenses, categories)