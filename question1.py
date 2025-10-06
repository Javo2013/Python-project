# question1.py
def calculate_budget():

    try:
        income = float(input("Enter your monthly income: $"))
    except ValueError:
        print("Invalid input. Please enter a number for income.")
        return

    try:
        rent = float(input("Enter rent expense: $"))
        food = float(input("Enter food expense: $"))
        entertainment = float(input("Enter entertainment expense: $"))
    except ValueError:
        print("Invalid input. Please enter numbers for expenses.")
        return

    total_expenses = rent + food + entertainment
    remaining = income - total_expenses

    print("\n=== BUDGET SUMMARY ===")
    print(f"Monthly Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Money: ${remaining:.2f}\n")

    if remaining < 0:
        advice = "You're overspending! Cut back on expenses."
    elif remaining < 100:
        advice = "Your budget is tight. Be careful with spending."
    else:
        advice = "Great job! You have money left over."

    print("Budget Advice:", advice)


if __name__ == "__main__":
    calculate_budget()