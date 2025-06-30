# TASK 1: Basic Calculator

# Arithmetic operation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

# Menu-driven loop
while True:
    print("\n📟 Basic Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    choice = input("Choose an option (0-4): ")

    if choice == "0":
        print("👋 Exiting calculator. Goodbye!")
        break

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                operation = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "*"
            elif choice == "4":
                result = divide(num1, num2)
                operation = "/"

            print(f"✅ Result: {num1} {operation} {num2} = {result:.2f}")

        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
        except ZeroDivisionError as e:
            print(f"❌ {e}")
    else:
        print("❌ Invalid choice. Please select a number from 0 to 4.")