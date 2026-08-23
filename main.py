from utils import show_menu, valid_input, clear_screen
from expense_manager import add_expenses, category_search
from file_manager import show_expenses, delete_all_expenses, update_expenses
from analytics import total_expenses, count_expenses, max_expense

name = input("Enter your name: ")
expenses = []
categories = []

def menu(expenses, categories):
    show_menu()

    option = valid_input("Enter your choice: ")

    if option == 1:
        add_expenses(expenses, categories)
        
    elif option == 2:
        show_expenses()
        
    elif option == 3:
        print(f"Total Expenses: {total_expenses(expenses)}")
        print()
        
    elif option == 4:
        print(f"You recorded {count_expenses(expenses)} expenses.")
        
    elif option == 5:
        if max_expense(expenses) == 0:
            print("No expenses recorded.")
        else:
            print(f"Highest Expense: {max_expense(expenses)}")
        
    elif option == 6: 
        category_search(categories, expenses)
        
    elif option == 7:
        delete_all_expenses()
            
    elif option == 8:
        exit()

    elif option == 9:
        clear_screen()

    else:
        print("Invalid choice. Try again.")
        
while True:
    update_expenses(expenses, categories)
    menu(expenses, categories)
    
if __name__ == "__main__":
    #Start the app