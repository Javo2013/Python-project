# question2.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # handle division by zero
    if b == 0:
        return None
    return a / b

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered. Please enter numeric values.")
        return

    print("Choose operation: 1. Add  2. Subtract  3. Multiply  4. Divide")
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        result = add(a, b)
        print(f"{a} + {b} = {result}")
    elif choice == "2":
        result = subtract(a, b)
        print(f"{a} - {b} = {result}")
    elif choice == "3":
        result = multiply(a, b)
        print(f"{a} * {b} = {result}")
    elif choice == "4":
        result = divide(a, b)
        if result is None:
            print("Error: Cannot divide by zero!")
        else:
            print(f"{a} ÷ {b} = {result}")
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()