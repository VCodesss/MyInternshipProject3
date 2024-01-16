import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, description, category):
        today = datetime.date.today()
        month_year = (today.month, today.year)

        if month_year not in self.expenses:
            self.expenses[month_year] = []

        self.expenses[month_year].append({'amount': amount, 'description': description, 'category': category})
        print("Expense added successfully!")

    def view_monthly_summary(self, month, year):
        month_year = (month, year)
        if month_year in self.expenses:
            total_expenses = sum(expense['amount'] for expense in self.expenses[month_year])
            print(f"Monthly Summary ({month}/{year}): Total Expenses: ${total_expenses}")
        else:
            print(f"No expenses recorded for {month}/{year}.")

    def view_category_expenditure(self, category):
        category_expenses = [expense['amount'] for expenses in self.expenses.values() for expense in expenses if
                             expense['category'].lower() == category.lower()]
        if category_expenses:
            total_category_expenses = sum(category_expenses)
            print(f"Category-wise Expenditure ({category}): Total Expenses: ${total_category_expenses}")
        else:
            print(f"No expenses recorded for the category: {category}.")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a brief description: ")
            category = input("Enter the expense category: ")
            tracker.add_expense(amount, description, category)
        elif choice == '2':
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            tracker.view_monthly_summary(month, year)
        elif choice == '3':
            category = input("Enter the category to view expenditure: ")
            tracker.view_category_expenditure(category)
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()