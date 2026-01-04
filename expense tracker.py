# Expense Tracker using Python

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Other): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")

    print("✅ Expense added successfully!")


def view_expenses():
    print("\n📋 All Expenses")
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date, category, amount, note = line.strip().split(",")
                print(f"Date: {date} | Category: {category} | Amount: ₹{amount} | Note: {note}")
    except FileNotFoundError:
        print("No expenses found.")


def total_expense():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                total += float(line.strip().split(",")[2])
        print(f"\n💰 Total Expense: ₹{total}")
    except FileNotFoundError:
        print("No expenses found.")


while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("👋 Exiting Expense Tracker. Bye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
