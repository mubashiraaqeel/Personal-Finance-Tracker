from finance import add_income, add_expense, view_transactions, edit_transaction, delete_transaction, search_transactions, budget_management
from reports import monthly_report, show_statistics

def welcome():
    print("==========================================================")
    print("                 PERSONAL FINANCE TRACKER                 ")
    print("==========================================================")
    print()
    print("Welcome to the Personal Finance Tracker")
    print()
    
def display_menu():
    print("-----------------------------------------------------------")
    print("                  Here is your menu bar :                  ")
    print("-----------------------------------------------------------")
    print()
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Edit Transaction")
    print("5. Delete Transaction")
    print("6. Search Transaction")
    print("7. Monthly Report")
    print("8. Show Statistics")
    print("9. Budget Management")
    print("10. Exit")
    
    
def get_user_choice():
    while True:
        try:
            choice = int(input("Choose an option (1-10): "))
            if 1 <= choice <= 10:
                return choice
            print("Invalid choice! Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 10.")
    
def main():
    #display welcome screen
    welcome()
    while True:
        #display menu bar
        display_menu()
        
        user = get_user_choice()
        
        if user == 1:
            add_income()
            print()
        elif user == 2:
            add_expense()
            print()
        elif user == 3:
            view_transactions()
            print()
        elif user == 4:
            edit_transaction()
            print()
        elif user == 5:
            delete_transaction()
            print()
        elif user == 6:
            search_transactions()
            print()
        elif user == 7:
            monthly_report()
            print()
        elif user == 8:
            show_statistics()
            print()
        elif user == 9:
            budget_management()
            print()  
        elif user == 10:
            print("==========================================================")
            print("Thank you for using Personal Finance Tracker.")
            print("Have a great day!")
            print("==========================================================")

            break
           
          
if __name__ == "__main__":
    main()