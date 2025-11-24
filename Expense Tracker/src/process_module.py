from helpers import format_currency


def view_expenses(expenses):
    print("--- All Expenses ---")
    if not expenses:
        print("No expenses found.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {format_currency(e['amount'])} | {e['category']} | {e['note']}")
    print()




def filter_by_category(expenses, category):
    print(f"--- Category: {category} ---")
    found = False
    for e in expenses:
        if e['category'] == category:
            print(f"{format_currency(e['amount'])} | {e['note']}")
    found = True
    if not found:
        print("No expenses in this category.")
    print()




def total_expense(expenses):
    total = sum(e['amount'] for e in expenses)
    print(f"Total spent: {format_currency(total)}")