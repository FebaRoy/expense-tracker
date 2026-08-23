def update_expenses(expenses, categories):
    categories.clear()
    expenses.clear()
    try: 
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                categories.append(line.split('|')[0].strip())
                expenses.append(float(line.split('|')[1].strip()))
    except FileNotFoundError:
        print("No expense file found. Starting refresh!")

def show_expenses():
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(f"Category: {line.split('|')[0].strip()}")
                print(f"Expense: {line.split('|')[1].strip()}")
                print()
    except FileNotFoundError:
        print("No expense file found. Starting refresh!")

def delete_all_expenses():
    try:
        with open("expenses.txt","w") as file:
            file.write("")
    except FileNotFoundError:
        print("No expense file found. Starting refresh!")
    print("All your expenses are deleted.")
