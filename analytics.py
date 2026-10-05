def total_expenses(expenditure):
    total = 0
    for expense in expenditure.values():
        total += expense
    return total

def count_expenses(expenditure):
    return len(expenditure)

def max_expense(expenditure):
    highest_expense = 0
    for expense in expenditure.values():
        if expense > highest_expense:
            highest_expense = expense
    return highest_expense
