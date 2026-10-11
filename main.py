import csv
import os

FILE_NAME = "expenses.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Amount", "Description"])


# Add Expense
def add_expense():
    category = input("Enter Category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, description])

    print("Expense Added Successfully!")


# View Expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n------ Expenses ------")
        for row in reader:
            print(row)


# Filter by Category
def filter_expense():
    category = input("Enter Category: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\nFiltered Expenses\n")

        found = False
        for row in reader:
            if row["Category"].lower() == category.lower():
                print(row)
                found = True

        if not found:
            print("No expenses found.")


# Category Summary
def summary():
    totals = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            totals[category] = totals.get(category, 0) + amount

    print("\nExpense Summary\n")

    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")


# Main Menu
def main():
    create_file()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expense()

        elif choice == "4":
            summary()

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


main()