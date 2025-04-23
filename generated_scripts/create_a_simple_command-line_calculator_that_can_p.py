
def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_number(prompt):
    """Function to get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    """Function to get a valid operation from user input."""
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in operations:
            return operations[op]
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def main():
    """Main function to run the calculator."""
    print("Simple Command-Line Calculator")
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        operation = get_operation()

        try:
            result = operation(num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)

        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
