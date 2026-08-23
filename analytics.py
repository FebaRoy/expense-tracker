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
