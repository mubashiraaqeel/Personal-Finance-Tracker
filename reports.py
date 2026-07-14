from finance import transactions

def calculate_balance(total_income, total_expense):
    return total_income - total_expense

def calculate_average(total, count):
    if count == 0:
        return 0
    else:
        return total / count

def monthly_report():
    while True:
        print("================================================")
        print("                 MONTHLY REPORT                 ")
        print("================================================")
        print()
        
        try:
            month = int(input("Enter month: "))
            if not (1 <= month <= 12):
                print("Month is not valid!")
                continue
        
            year = int(input("Enter year:"))
            if year <= 0:
                print("Year is not valid!")
                continue
            
            total_income = 0
            total_expense = 0
            
            found = False
            
            for transaction in transactions:
                
                transaction_year, transaction_month, transaction_day = transaction["Date"].split("-") 
                
                transaction_year = int(transaction_year)
                transaction_month = int(transaction_month)
                
                if year == transaction_year and month == transaction_month:
                 
                    found = True
                   
                    if transaction["Type"] == "Income":
                        total_income += transaction["Amount"]
                    elif transaction["Type"] == "Expense":
                        total_expense += transaction["Amount"]
                
            balance = calculate_balance(total_income, total_expense)
            
            if not found:
                print("No transactions found for the selected month and year.")
                break
            
            print("================================================")
            print("                  REPORT SUMMARY                ")
            print("================================================")
            print()   
            print("Month         : ",month)
            print("Year          : ",year)           
            print("Total Income  : Rs.", total_income)
            print("Total Expense : Rs.", total_expense)
            print("Total Balance : Rs.", balance) 
            print("-------------------------------------------------")
            break
        
        
        except Exception as e:
            print("ERROR:", e)
            
            
            

def show_statistics():
    
    print("=================================================")
    print("                 SHOW STATISTICS                 ")
    print("=================================================")
    print()
    
    if len(transactions) == 0:
        print("No Transaction Found!")
        return
    
    total_income = 0
    total_expense = 0
    income_count = 0
    expense_count = 0
    
    for transaction in transactions:
        
         if transaction["Type"] == "Income":
            total_income += transaction["Amount"]
            income_count += 1
            
         elif transaction["Type"] == "Expense":
             total_expense += transaction["Amount"]
             expense_count += 1 
             
    balance = calculate_balance(total_income, total_expense)
    
    total_transactions = income_count + expense_count
    
    avrg_income = calculate_average(total_income, income_count)
    avrg_expense = calculate_average(total_expense, expense_count)    
    
    print("==================================================")
    print("               FINANCIAL STATISTICS               ")
    print("==================================================")
    print()
    print("Total Transactions   : ", total_transactions)
    print("Income Entries       : ", income_count)
    print("Expense Entries      : ", expense_count)
    print()
    print("Total Income         : Rs.", total_income)
    print("Total Expense        : Rs.", total_expense)
    print("Current Balance      : Rs.", balance)
    print()
    print(f"Average Income       : Rs. {avrg_income:.2f}")
    print(f"Average Expense      : Rs. {avrg_expense:.2f}")
    print("---------------------------------------------------")