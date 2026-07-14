from datetime import datetime
from storage import save_data, load_data

monthly_budget, transactions = load_data()

income_categories = {1: "Salary", 2: "Freelancing",
                         3: "Business", 4: "Gift",
                         5: "Investment", 6: "Other" }

expense_categories = {1: "Food", 2: "Transport",
                                  3: "Shopping", 4: "Bills",
                                  5: "Entertainment", 6: "Healthcare",
                                  7: "Education" , 8: "Other"}
 

   
def add_income():
    while True:
        
        print("==========================================================")
        print("                        ADD INCOME                        ")
        print("==========================================================")
        print()
        
        try:
            income = float(input("Enter Amount: "))
            if income <= 0 :
                print("Invalid Amount!")
                continue
            
            print("-----------------------------------------------------------")
            print("                     Income Categories                     ")
            print("-----------------------------------------------------------")
            print("1. Salary") 
            print("2. Freelancing") 
            print("3. Business") 
            print("4. Gift") 
            print("5. Investment") 
            print("6. Other") 
            print()
            
            try:
                category_choice = int(input("Enter an option (1-6): "))
                if category_choice not in income_categories:
                    print("Invalid category choice!")
                    continue 
                category_name = income_categories[category_choice]
                    
                 
                description = input("Enter description: ")
                description = description.strip()
                if description == "":
                    print("Invalid Description!")
                    continue 
                    
                
                date = input("Enter date (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")
                
                dictionary = {"Type"        : "Income", 
                              "Amount"      : income,
                              "Category"    : category_name,
                              "Description" : description,
                              "Date"        : date}
                
                transactions.append(dictionary)
                print("==========================================================")
                print("                Income Added Successfully!                ")
                print("==========================================================")
                save_data(transactions, monthly_budget)
                break
          
            except ValueError:
                print("Invalid Input!")
    
        except ValueError:
            print("Invalid Amount!")
        
           

def add_expense():
    
    while True:
        
        print("===========================================================")
        print("                        ADD EXPENSE                        ")
        print("===========================================================")
        print()
        
        try:
            expense = float(input("Enter Amount: "))
            if expense <= 0 :
                print("Invalid Amount!")
                continue
            
            print("-----------------------------------------------------------")
            print("                     Expense Categories                     ")
            print("-----------------------------------------------------------")
            print("1. Food") 
            print("2. Transport") 
            print("3. Shopping") 
            print("4. Bills") 
            print("5. Entertainment") 
            print("6. Healthcare")
            print("7. Education")
            print("8. Other") 
            print()
            
            try:
                category_choice = int(input("Enter an option (1-8): "))
                if category_choice not in expense_categories:
                    print("Invalid category choice!")
                    continue 
                category_name = expense_categories[category_choice]
                    
                 
                description = input("Enter description: ")
                description = description.strip()
                if description == "":
                    print("Invalid description!")
                    continue 
                    
                
                date = input("Enter date (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")
                
                dictionary = {"Type"        : "Expense", 
                              "Amount"      : expense,
                              "Category"    : category_name,
                              "Description" : description,
                              "Date"        : date}
                
                transactions.append(dictionary)
                print("===========================================================")
                print("                Expense Added Successfully!                ")
                print("===========================================================")
                save_data(transactions, monthly_budget)
                break
          
            except ValueError:
                print("Invalid Input!")
    
        except ValueError:
            print("Invalid Amount!")
    
        
def display_transactions():
    
    if len(transactions) == 0:
        print("No Transaction Found!")
        return
    else:   
        count_transaction = 1
        
        for transaction in transactions:
            print("-----------------------------------------------------------")
            print("            Transaction # ",count_transaction)
            print("-----------------------------------------------------------")
            print()
            print("Type         :", transaction["Type"])
            print("Amount       : Rs.", transaction["Amount"])
            print("Category     :", transaction["Category"])
            print("Description  :", transaction["Description"])
            print("Date         :", transaction["Date"])
            print("-----------------------------------------------------------")
            count_transaction += 1
    
    
def view_transactions():
    
    print("==========================================================")
    print("                     VIEW TRANSACTIONS                     ")
    print("==========================================================")
    print()
        
    display_transactions()
            
            
                
                
def edit_transaction():
    while True:
        print("==========================================================")
        print("                     EDIT TRANSACTION                     ")
        print("==========================================================")
        print()
        
        display_transactions()

        if len(transactions) == 0:
            break
                
        try:
            transaction_no = int(input("Enter transaction no : "))
            if transaction_no >= 1 and transaction_no <= len(transactions):
                selected_transaction = transactions[transaction_no-1]
                print("------------------------------------------")
                print("What do you want to edit?")
                print("------------------------------------------")
                print("1. Amount ")
                print("2. Category")
                print("3. Description")
                print("4. Date")
                print("5. Cancel")
                print("------------------------------------------")
                
                edit_dictionary = {1 : "Amount", 
                                   2 : "Category", 
                                   3 : "Description", 
                                   4 : "Date", 
                                   5 : "Cancel"}
                
                edit_option = int(input("Enter an option (1-5): "))
                
                if edit_option not in edit_dictionary:
                    print("Invalid option!")
                    continue
                
                if edit_option == 1:
                    amount = float(input("Enter new amount: "))
                    if amount <= 0 :
                        print("Invalid Amount!")
                        continue
                    selected_transaction["Amount"] = amount
                    print("Amount updated successfully!")
                    save_data(transactions, monthly_budget)
                    break

                elif edit_option == 2:
                    
                    category = input("Enter new category: ").title()
                    
                    if selected_transaction["Type"] == "Income":
                        if category not in income_categories.values():
                            print("Invalid category choice!")
                            continue

                    elif selected_transaction["Type"] == "Expense":
                        if category not in expense_categories.values():
                            print("Invalid category choice!")
                            continue
                    
                    selected_transaction["Category"] = category
                    print("Category updated successfully!")
                    save_data(transactions, monthly_budget)
                    break

                elif edit_option == 3:
                    description = input("Enter new description: ")
                    description = description.strip()
                    if description == "":
                        print("Invalid Description!")
                        continue 
                    selected_transaction["Description"] = description
                    print("Description updated successfully!")
                    save_data(transactions, monthly_budget)
                    break
                    
                elif edit_option == 4:
                    date = input("Enter new date (YYYY-MM-DD): ")
                    datetime.strptime(date, "%Y-%m-%d")
                    selected_transaction["Date"] = date
                    print("Date updated successfully!")
                    save_data(transactions, monthly_budget)
                    break
                    
                elif edit_option == 5:
                    print("Edit cancelled.")
                    break
                        
            else:
                print("Invalid number!")
                        
        except ValueError:
            print("Invalid Input!")
                    
                        
    
    
    

def delete_transaction():
        
    print("==========================================================")
    print("                    DELETE TRANSACTION                    ")
    print("==========================================================")
    print()

    display_transactions()

    if len(transactions) == 0:
        return
    
    try:
        transaction_no = int(input("Enter transaction no : "))
        if transaction_no >= 1 and transaction_no <= len(transactions):
            selected_transaction = transactions[transaction_no-1]
            transactions.remove(selected_transaction)
            save_data(transactions, monthly_budget)
            print("==================================================")
            print("       ✓ Transaction deleted successfully!        ")
            print("==================================================")
                        
        else:
            print("Invalid number!")
                        
    except ValueError:
        print("Invalid Input!")
            
    
    
    
def display_transaction(transaction):
    
    print("------------------------------------------------")
    print("Type        :", transaction["Type"])
    print("Amount      : Rs.", transaction["Amount"])
    print("Category    :", transaction["Category"])
    print("Description :", transaction["Description"])
    print("Date        :", transaction["Date"])
    print("------------------------------------------------")
    
def search_transactions():
    while True:
        print("===========================================================")
        print("                    SEARCH TRANSACTIONS                    ")
        print("===========================================================")
        print()
        if len(transactions) == 0:
            print("No Transaction Found!")
            break
        
        print("1. Search by Type ")
        print("2. Search by Category")
        print("3. Search by Description")
        print("4. Search by Date")
        print("5. Cancel")
        print("------------------------------------------")
        search_menu = {1 : "Search by Type",
                       2 : "Search by Category",
                       3 : "Search by Description",
                       4 : "Search by Date",
                       5 : "Cancel"}
        try:
            search_choice = int(input("Enter an option (1-5): "))
            if search_choice not in search_menu:
                print("Invalid search choice!")
                continue
            else:
                if search_choice == 1:
                    type_name = input("Enter type name: ")
                    
                    found = False
                        
                    for transaction in transactions:
                        if transaction["Type"].lower() == type_name.lower() :
                            found = True
                            
                            print("Transaction Found")
                            display_transaction(transaction) 
                    if not found:
                        print("Transaction Not Found!")
                        
                        
                elif search_choice == 2:
                    category_name = input("Enter category name: ")
                    
                    found = False
                    
                    for transaction in transactions:
                        if transaction["Category"].lower() == category_name.lower():
                            found = True
                            print("Transaction Found")
                            display_transaction(transaction) 
                   
                    if not found:
                        print("Transaction Not Found!")
                        
                        
                elif search_choice == 3:
                    add_description = input("Enter description: ")
                    
                    found = False
                    
                    for transaction in transactions:
                        if transaction["Description"].lower() == add_description.lower():
                            found = True
                            
                            print("Transaction Found")                           
                            display_transaction(transaction) 
                    
                    if not found:
                        print("Transaction Not Found!")
                        
                        
                elif search_choice == 4:
                    add_date = input("Enter date (YYYY-MM-DD) : ")
                    
                    found = False
                    for transaction in transactions:
                        if transaction["Date"] == add_date:
                            found = True
                            
                            print("Transaction Found")
                            display_transaction(transaction)
                    if not found:
                        print("Transaction Not Found!")
                        
                        
                elif search_choice == 5:
                    print("Search Cancelled!")
                    break
                
                
        except ValueError:
            print("Invalid Input!")
        
              


def budget_management():
    
    global monthly_budget
    
    while True:
        print("===========================================================")
        print("                     BUDGET MANAGEMENT                     ")
        print("===========================================================")
        print()
        print("1. Set Budget")
        print("2. View Budget Status")
        print("3. Back")
        
        budget_choice = {1 : "Set Budget",
                         2 : "View Budget Status",
                         3 : "Back"}
        
        try:
            budget_option = int(input("Enter an option (1-3): "))
            if budget_option not in budget_choice:
                print("Invalid option!")
                continue
                
            
            if budget_option == 1:
            
                monthly_budget = float(input("Enter budget: "))
                if monthly_budget <= 0:
                    print("Budget must be greater than 0!")
                    continue
                save_data(transactions, monthly_budget)
                           
                print("==========================================================")
                print("                 Set budget successfully!                 ")
                print("==========================================================")
                
                
            elif budget_option == 2:
                
                if monthly_budget == 0:
                    print("Please set a budget first!")
                    continue
                
                total_expense = 0 
                               
                for transaction in transactions:
                    
                    if transaction["Type"].lower() == "expense":
                        total_expense += transaction["Amount"]
            
                remaining_budget = monthly_budget - total_expense
                
                print("==========================================================")
                print("                    VIEW BUDGET STATUS                    ")
                print("==========================================================")
            
                print("Budget           : Rs.", monthly_budget)
                print("Total Expense    : Rs.", total_expense)
                print("Remaining Budget : Rs.", remaining_budget)
                
                if total_expense > monthly_budget:
                    print("⚠ Warning! You have exceeded your budget.")
                elif total_expense == monthly_budget:
                    print("You have used your entire budget.")
                else:
                    print("You are within your budget.")
                   
            elif budget_option == 3:
                break  
        
        except ValueError:
            print("Invalid Input!")        