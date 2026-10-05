def update_expenses(expenditure):
    expenditure.clear()
    try: 
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.split('|')
                expense = float(line[1].strip())
                category = line[0].strip()
                expenditure[category] = expenditure.get(category, 0) + expense
                highest_categories = [i for i in expenditure if expenditure[i] > 1000]
            return highest_categories
    except FileNotFoundError:
        print("No expense file found. Starting refresh!")

def show_high_spending_categories(expenditure):
    highest_categories = update_expenses(expenditure)
    if highest_categories:
        print("High spending categories:")
        for category in highest_categories:
            print(f"{category} with expense {expenditure[category]}")
    else:
        print("No high spending categories found.")

def show_expenses():
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.split('|')
                print(f"Category: {line[0].strip()}")
                print(f"Expense: {line[1].strip()}")
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
