def get_expense_from_user():
  print("--- Add Expense ---")
  try:
    amount = float(input("Enter amount: ").strip())
  except:
    print("Invalid amount. Try again.")
    return None
  category = input("Enter category (food/travel/etc.): ").strip().lower()
  note = input("Enter a short note: ").strip()
  return {"amount": amount,"category": category,"note": note}