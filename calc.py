def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

print("Simple Calculator")
while True:
    print()
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")
    choice = input("Choose an option: ")
    if choice == "5":
        print("Goodbye!")
        break
    num1 = get_number("First number: ")
    num2 = get_number("Second number: ")
    if choice == "1":
        print("Answer:", add(num1, num2))
    elif choice == "2":
        print("Answer:", subtract(num1, num2))
    elif choice == "3":
        print("Answer:", multiply(num1, num2))
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Answer:", divide(num1, num2))
    else:
        print("Invalid choice.")