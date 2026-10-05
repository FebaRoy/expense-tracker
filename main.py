from utils import show_menu, valid_input, clear_screen
from expense_manager import add_expenses, category_search
from file_manager import show_expenses, delete_all_expenses, show_high_spending_categories, update_expenses
from analytics import total_expenses, count_expenses, max_expense

name = input("Enter your name: ")
expenditure = {}

def menu(expenditure):
    show_menu()

    option = valid_input("Enter your choice: ")

    if option == 1:
        add_expenses(expenditure)
        
    elif option == 2:
        show_expenses()
        
    elif option == 3:
        print(f"Total Expenses: {total_expenses(expenditure)}")
        print()
        
    elif option == 4:
        print(f"You recorded {count_expenses(expenditure)} expenses.")
        
    elif option == 5:
        if max_expense(expenditure) == 0:
            print("No expenses recorded.")
        else:
            print(f"Highest Expense: {max_expense(expenditure)}")
        
    elif option == 6: 
        category_search(expenditure)
        
    elif option == 7:
        show_high_spending_categories(expenditure)
        
    elif option == 8:
        delete_all_expenses()
            
    elif option == 9:
        exit()

    elif option == 10:
        clear_screen()

    else:
        print("Invalid choice. Try again.")
        
while True:
    update_expenses(expenditure)
    menu(expenditure)
    
# if __name__ == "__main__":
#     #Start the app