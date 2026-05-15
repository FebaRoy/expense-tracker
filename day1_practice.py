name = input("Enter your name: ")
# expense = float(input("Enter your total expense: "))
expenses = []
# category = input("Enter the category of your expense: ")
categories = []

file = open("expenses.txt", "w")

for i in range(3):
    expense = float(input(f"Enter your expense {i+1}: "))
    category = input(f"Enter the category of your expense {i+1}: ")
    if expense > 1000:
        print(f"{expense} is a high expense.")
    expenses.append(expense)
    categories.append(category)

def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total = total + expense
    return total

def count_expenses(expenses):
    count = 0
    for expense in expenses:
        count += 1
    return count

def max_expense(expenses):
    max = 0
    for expense in expenses:
        if expense > max:
            max = expense
    return max

def food_expenses(categories):
    food = 0
    for category in categories:
        if str(category).lower() == "food":
            food += 1
    return food

def travel_expenses(categories):
    travel = 0
    for category in categories:
        if str(category).lower() == "travel":
            travel += 1
    return travel

for i in range(len(expenses)):
    file.write(f"{categories[i]} | {expenses[i]}\n")
file.close()

print("-----Expense Recorded-----")
print(f"Name: {name}")
# print(f"Expenses: {expenses}")
# print(f"Categories: {categories}")
file = open("expenses.txt", "r")
print(file.read())
print(f"You recorded {count_expenses(expenses)} expenses.")
print(f"Total Expenses: {total_expenses(expenses)}")
print(f"Highest Expense: {max_expense(expenses)}")
print(f"Food Expenses: {food_expenses(categories)}")
print(f"Travel Expenses: {travel_expenses(categories)}")