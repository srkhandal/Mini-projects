def expensetracker():
    print("\n_______________ Dynamic Expense Tracker ____________________")
    
    categories = ["Grocery", "Transport", "Education", "Electricity", "Water", "Gas","others"]
    
    category_values = {}
    print("\nCategories:")
    for category in categories:
                print(f"  - {category}")
                
    print("\nMonthly Expense Limit(MEL)")
    MEL = float(input("enter the MEL: "))
    
         
    print("\nEnter the amount in categories")
    for category in categories:
        while True:
            amount=float(input(f" {category}: Rs "))
            category_values[category] = amount
            print(f"Added Rs {amount:.2f} to {category}.\n")
            break
        
    print("\nExpense summary:")
    total_expenses = sum(category_values.values())
    if(total_expenses == 0):
        print("No expenses recorded")
    else:
        for category, amount in category_values.items():
            percentage = (amount/total_expenses)*100
            print(f"  {category}: Rs.{amount:.2f} ({percentage:.2f}%)")
        
        print(f"\nTotal Expenses: Rs.{total_expenses:.2f}")
        if(MEL>total_expenses):
            print(f"Your Monthly expense is Rs {total_expenses} which is in limit.")
        else:
            print(f"Your total expenses is exceeeding the monthly expense limit by {total_expenses-MEL}." )
        
        
if __name__ == "__main__":
    expensetracker()




 