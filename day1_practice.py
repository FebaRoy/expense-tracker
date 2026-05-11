name = input("Enter your name: ")
# expense = float(input("Enter your total expense: "))
expenses = []
# category = input("Enter the category of your expense: ")
categories = []

for i in range(3):
    expense = float(input(f"Enter your expense {i+1}: "))
    category = input(f"Enter the category of your expense {i+1}: ")
    expenses.append(expense)
    categories.append(category)

def total_expenses(expenses):
    total = 0
    for i in range(len(expenses)):
        total = total + expenses[i]
    return total

print(f"Expenses: {expenses}")
print(f"Categories: {categories}")
print(f"Total Expenses: {total_expenses(expenses)}")

# if expense > 1000:
#     print("Warning: High spending!")
# else:
#     print("Spending is under control!")

# if category.lower() == "food":
#     print("Food expense recorded.")
# elif category.lower() == "travel":
#     print("Travel expense recorded.")
# else:
#     print("Expense recorded successfully")

# print("-----Expense Recorded-----")
# print(f"Name: {name}")
# print(f"Amount:  {expense}")
# print(f"Category: {category}")
