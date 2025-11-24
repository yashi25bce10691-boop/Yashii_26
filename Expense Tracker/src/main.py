from storage_module import load_expenses, save_expenses
from input_module import get_expense_from_user
from process_module import view_expenses, filter_by_category, total_expense




def main():
    expenses = load_expenses()
    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Total Expenditure")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            exp = get_expense_from_user()
            if exp:
                expenses.append(exp)
                save_expenses(expenses)
                print("Saved!")
        elif choice == "2":
                view_expenses(expenses)
        elif choice == "3":
                cat = input("Category to filter: ").strip().lower()
                filter_by_category(expenses, cat)
        elif choice == "4":
                total_expense(expenses)
        elif choice == "5":
                print("Goodbye!")
                break
        else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()